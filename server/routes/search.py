from datetime import datetime, timezone
from fastapi import APIRouter, Depends
from sqlalchemy import asc, desc, func, literal_column, select
from sqlalchemy.ext.asyncio import AsyncSession

from db.session_fabric import get_session
from models.title.meta import TitleMeta
from models.title.rate import TitleRate
from models.title.view import TitleView
from schemas.catalog import SearchPostScheme, SearchResultScheme
from schemas.title import TitleMetaScheme


router = APIRouter()


@router.post("/title")
async def search_title(
    scheme: SearchPostScheme,
    session: AsyncSession = Depends(get_session),
) -> SearchResultScheme:
    page = max(0, scheme.index)
    limit = 50

    views_count_subq = (
        select(TitleView.title_id, func.count(TitleView.id).label("views_count"))
        .group_by(TitleView.title_id)
        .subquery()
    )
    avg_rating_subq = (
        select(
            TitleRate.title_id,
            func.coalesce(func.avg(TitleRate.rating), 0).label(
                "avg_rating"
            ),  # Coalesce добавлен здесь
        )
        .group_by(TitleRate.title_id)
        .subquery()
    )
    query = (
        select(
            TitleMeta,
            func.coalesce(views_count_subq.c.views_count, 0).label("views_count"),
            avg_rating_subq.c.avg_rating,
        )
        .join(avg_rating_subq, TitleMeta.id == avg_rating_subq.c.title_id, isouter=True)
        .join(views_count_subq, TitleMeta.id == views_count_subq.c.title_id, isouter=True)
    )

    if scheme.rate_min is not None:
        query = query.where(avg_rating_subq.c.avg_rating >= scheme.rate_min)

    if scheme.rate_max is not None:
        query = query.where(avg_rating_subq.c.avg_rating <= scheme.rate_max)

    if scheme.prompt:
        query = query.where(
            TitleMeta.title_ru.ilike(f"%{scheme.prompt}%")
            or TitleMeta.title_en.ilike(f"%{scheme.prompt}%")
            or TitleMeta.title_jp.ilike(f"%{scheme.prompt}%")
            or TitleMeta.title_an.ilike(f"%{scheme.prompt}%")
        )

    if scheme.release_year_min is not None:
        query = query.where(TitleMeta.release_year >= scheme.release_year_min)

    if scheme.release_year_max is not None:
        query = query.where(TitleMeta.release_year <= scheme.release_year_max)

    if scheme.include_tags:
        for tag in scheme.include_tags:
            query = query.where(
                func.array_to_string(func.string_to_array(TitleMeta.tags, "/"), ",").contains(
                    str(tag)
                )
            )

    if scheme.exclude_tags:
        for tag in scheme.exclude_tags:
            query = query.where(
                ~func.array_to_string(func.string_to_array(TitleMeta.tags, "/"), ",").contains(
                    str(tag)
                )
            )

    if scheme.include_genres:
        for genre in scheme.include_genres:
            query = query.where(
                func.array_to_string(func.string_to_array(TitleMeta.genres, "/"), ",").contains(
                    str(genre)
                )
            )

    if scheme.exclude_genres:
        for genre in scheme.exclude_genres:
            query = query.where(
                ~func.array_to_string(func.string_to_array(TitleMeta.genres, "/"), ",").contains(
                    str(genre)
                )
            )

    column = TitleMeta.release_year
    if scheme.sort_by_views:
        column = literal_column("views_count")
    elif scheme.sort_by_rating:
        column = literal_column("avg_rating")

    if scheme.descending_order:
        query = query.order_by(desc(column))
    else:
        query = query.order_by(asc(column))

    count = query
    query = query.offset((page) * limit).limit(limit)

    async with session:
        exec = (await session.execute(query)).scalars().all()
        length = len((await session.execute(count)).scalars().all())
        total_pages = (length + limit - 1) // limit

        metas: list[TitleMetaScheme] = []

        for title in exec:
            tags = []
            genres = []

            for t in title.tags.split("/") if title.tags is not None else []:
                try:
                    tags.append(int(t))
                except Exception:
                    continue

            for g in title.genres.split("/") if title.genres is not None else []:
                try:
                    genres.append(int(g))
                except Exception:
                    continue

            meta = TitleMetaScheme(
                id=title.id,
                title_id=title.title_id,
                title_ru=title.title_ru,
                title_en=title.title_en,
                title_jp=title.title_jp,
                title_an=title.title_an,
                description=title.description,
                author_id=title.author_id,
                artist_id=title.artist_id,
                publisher_id=title.publisher_id,
                tags=tags,
                genres=genres,
                approved=True,
                approved_at=datetime.now(timezone.utc),
                approved_user_uuid="",
                created_user_uuid="",
                created_at=datetime.now(timezone.utc),
                release_year=title.release_year,
            )

            metas.append(meta)

        return SearchResultScheme(
            end=page <= total_pages,
            titles=metas,
        )
