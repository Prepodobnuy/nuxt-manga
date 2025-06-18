from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import Float, asc, desc, func, literal_column, or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from db.session_fabric import get_session
from models.title.meta import TitleMeta
from models.title.rate import TitleRate
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

    avg_rating_subquery = (
        select(
            TitleRate.title_id, func.coalesce(func.avg(TitleRate.rating), None).label("avg_rating")
        )
        .group_by(TitleRate.title_id)
        .subquery()
    )
    query = select(TitleMeta, avg_rating_subquery.c.avg_rating).join(
        avg_rating_subquery, TitleMeta.title_id == avg_rating_subquery.c.title_id, isouter=True
    )

    if scheme.rate_min:
        query = query.where(avg_rating_subquery.c.avg_rating >= scheme.rate_min)

    if scheme.rate_max:
        query = query.where(avg_rating_subquery.c.avg_rating <= scheme.rate_max)

    if scheme.prompt:
        query = query.where(
            or_(
                TitleMeta.title_ru.ilike(f"%{scheme.prompt}%"),
                TitleMeta.title_en.ilike(f"%{scheme.prompt}%"),
                TitleMeta.title_jp.ilike(f"%{scheme.prompt}%"),
                TitleMeta.title_an.ilike(f"%{scheme.prompt}%"),
            )
        )

    print(scheme.include_tags)
    if scheme.include_tags:
        for tag in scheme.include_tags:
            query = query.where(TitleMeta.tags.contains(f"{tag}"))

    if scheme.exclude_tags:
        for tag in scheme.exclude_tags:
            query = query.where(~TitleMeta.tags.contains(f"{tag}"))

    if scheme.include_genres:
        for genre in scheme.include_genres:
            query = query.where(TitleMeta.genres.contains(f"{genre}"))

    if scheme.exclude_genres:
        for genre in scheme.exclude_genres:
            query = query.where(~TitleMeta.genres.contains(f"{genre}"))

    if scheme.descending_order:
        query = query.order_by(
            desc(avg_rating_subquery.c.avg_rating).nulls_last(),
        )
    else:
        query = query.order_by(
            asc(avg_rating_subquery.c.avg_rating).nulls_last(),
        )

    count_query = select(func.count()).select_from(query.alias())
    query = query.offset((page) * limit).limit(limit)

    async with session:
        exec = (await session.execute(query)).scalars().all()

        total_count = await session.scalar(count_query) or 0
        total_pages = (total_count + limit - 1) // limit

        metas: list[TitleMetaScheme] = []

        for title in exec:
            tags = [int(t) for t in title.tags.split("/") if t.isdigit()] if title.tags else []
            genres = (
                [int(g) for g in title.genres.split("/") if g.isdigit()] if title.genres else []
            )

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
