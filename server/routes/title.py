import json
from typing import Literal
from fastapi import APIRouter, Depends, File, Form, HTTPException, Request, UploadFile
from models.assets.title import TitleCover
from pydantic import BaseModel, ValidationError
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.session_fabric import get_session
from models.title.list import TitleList
from models.title.meta import TitleMeta
from models.title.rate import TitleRate
from models.title.title import Title
from models.title.view import TitleView
from models.user.user import User
from modules.auth import get_moder, get_user
from schemas.title import (
    TitleListScheme,
    TitleMetaPostScheme,
    TitleMetaScheme,
    TitleRateGetScheme,
    TitleUserRateScheme,
)
from services.title.asset import TitleAssetService
from services.title.meta import TitleMetaService
from services.title.title import TitleService


router = APIRouter()


@router.get("/search/{prompt}")
async def quick_search(
    prompt: str,
    session: AsyncSession = Depends(get_session),
) -> list[TitleMetaScheme]:
    async with session:
        query = (
            select(TitleMeta)
            .where(
                TitleMeta.approved == True,
                TitleMeta.title_ru.ilike(f"%{prompt}%")
                | TitleMeta.title_en.ilike(f"%{prompt}%")
                | TitleMeta.title_jp.ilike(f"%{prompt}%")
                | TitleMeta.title_an.ilike(f"%{prompt}%"),
            )
            .limit(10)
        )

        exec = await session.execute(query)

        res = []
        for m in exec.scalars().all():
            res.append(TitleMetaService(m).to_scheme())

        return res


@router.get("/{id}/meta")
async def get_title_meta(
    id: int,
    session: AsyncSession = Depends(get_session),
) -> TitleMetaScheme:
    print("\n\n\n\n\n", id, "\n\n\n\n\n")
    exec = await session.execute(
        select(TitleMeta).where(
            TitleMeta.title_id == id,
            TitleMeta.approved == True,
        )
    )
    meta = exec.scalar_one_or_none()
    if meta is None:
        raise HTTPException(404)

    return TitleMetaService(meta=meta).to_scheme()


@router.get("/{id}/rates")
async def get_title_rates(
    id: int,
    session: AsyncSession = Depends(get_session),
) -> TitleRateGetScheme:
    exec1 = await session.execute(
        select(TitleRate).where(TitleRate.rating == 1, TitleRate.title_id == id)
    )
    exec2 = await session.execute(
        select(TitleRate).where(TitleRate.rating == 2, TitleRate.title_id == id)
    )
    exec3 = await session.execute(
        select(TitleRate).where(TitleRate.rating == 3, TitleRate.title_id == id)
    )
    exec4 = await session.execute(
        select(TitleRate).where(TitleRate.rating == 4, TitleRate.title_id == id)
    )
    exec5 = await session.execute(
        select(TitleRate).where(TitleRate.rating == 5, TitleRate.title_id == id)
    )

    return TitleRateGetScheme(
        rates_1=len(exec1.scalars().all()),
        rates_2=len(exec2.scalars().all()),
        rates_3=len(exec3.scalars().all()),
        rates_4=len(exec4.scalars().all()),
        rates_5=len(exec5.scalars().all()),
    )


@router.get("/{id}/rate")
async def get_my_title_rate(
    id: int,
    session: AsyncSession = Depends(get_session),
    user: User = Depends(get_user),
) -> TitleUserRateScheme:
    exec = await session.execute(
        select(TitleRate).where(
            TitleRate.user_uuid == user.uuid,
            TitleRate.title_id == id,
        )
    )
    trate = exec.scalar_one_or_none()
    if trate is None:
        return TitleUserRateScheme(rate=None)

    return TitleUserRateScheme(rate=trate.rating)


@router.get("/{id}/lists")
async def get_title_list(
    id: int,
    session: AsyncSession = Depends(get_session),
) -> TitleListScheme:
    exec1 = await session.execute(
        select(TitleList).where(
            TitleList.title_id == id,
            TitleList.name == "__READING__",
        )
    )
    exec2 = await session.execute(
        select(TitleList).where(
            TitleList.title_id == id,
            TitleList.name == "__PLANNED__",
        )
    )
    exec3 = await session.execute(
        select(TitleList).where(
            TitleList.title_id == id,
            TitleList.name == "__GRAVEYARD__",
        )
    )
    exec4 = await session.execute(
        select(TitleList).where(
            TitleList.title_id == id,
            TitleList.name == "__READED__",
        )
    )
    exec5 = await session.execute(
        select(TitleList).where(
            TitleList.title_id == id,
            TitleList.name == "__LOVED__",
        )
    )
    exec6 = await session.execute(
        select(TitleList).where(
            TitleList.title_id == id,
            TitleList.name != "__READING__",
            TitleList.name != "__PLANNED__",
            TitleList.name != "__GRAVEYARD__",
            TitleList.name != "__READED__",
            TitleList.name != "__LOVED__",
        )
    )

    return TitleListScheme(
        reading=len(exec1.scalars().all()),
        planned=len(exec2.scalars().all()),
        graveyard=len(exec3.scalars().all()),
        readed=len(exec4.scalars().all()),
        loved=len(exec5.scalars().all()),
        another=len(exec6.scalars().all()),
    )


@router.post("/")
async def post_title(
    request: Request,
    user: User = Depends(get_moder),
    session: AsyncSession = Depends(get_session),
):
    try:
        form_data = await request.form()
        scheme_data = form_data.get("scheme")

        if scheme_data is None:
            raise HTTPException(status_code=400, detail="Missing scheme data")
        scheme_data = scheme_data

        try:
            scheme_json = json.loads(scheme_data)
            title_data = TitleMetaPostScheme(**scheme_json)
        except json.JSONDecodeError:
            raise HTTPException(status_code=400, detail="Invalid JSON in scheme")
        except ValidationError as e:
            raise HTTPException(status_code=422, detail=e.errors())

        files = []
        for key in form_data.keys():
            if key.startswith("file"):
                print(key)
                files.append(form_data[key])

        if not files:
            raise HTTPException(status_code=400, detail="At least one cover file is required")

        async with session:
            try:
                title = TitleService.create(user=user)
                session.add(title)
                print("\n", title)

                await session.flush()
                meta = TitleMetaService.create_from_scheme(
                    title=title, user=user, scheme=title_data
                )
                meta.approved = True
                session.add(meta)
                await session.flush()
                print("\n", meta)

                i = 0
                for file in files:
                    contents = await file.read()
                    try:
                        await TitleAssetService(title=title).set_cover(
                            data=contents, order=i, session=session
                        )
                        i += 1
                    except ValueError:
                        continue

                if i == 0:
                    raise ValueError

                await session.commit()

            except Exception as e:
                print(e)
                await session.rollback()
                raise HTTPException(500)

    except Exception as e:
        print(e)
        raise HTTPException(500)


@router.post("/{id}/update")
async def post_update_title(
    id: int,
    request: Request,
    user: User = Depends(get_moder),
    session: AsyncSession = Depends(get_session),
):
    try:
        form_data = await request.form()
        scheme_data = form_data.get("scheme")

        if scheme_data is None:
            raise HTTPException(status_code=400, detail="Missing scheme data")
        scheme_data = scheme_data

        try:
            scheme_json = json.loads(scheme_data)
            title_data = TitleMetaPostScheme(**scheme_json)
        except json.JSONDecodeError:
            raise HTTPException(status_code=400, detail="Invalid JSON in scheme")
        except ValidationError as e:
            raise HTTPException(status_code=422, detail=e.errors())

        query = select(Title).where(Title.id == id)
        meta_query = select(TitleMeta).where(TitleMeta.title_id == id)

        async with session:
            try:
                title = (await session.execute(query)).scalar_one_or_none()
                if title is None:
                    raise HTTPException(404)

                meta = (await session.execute(meta_query)).scalar_one_or_none()
                if meta is None:
                    meta = TitleMetaService.create_from_scheme(
                        title=title, user=user, scheme=title_data
                    )

                meta.approved = True
                meta.title_ru = title_data.title_ru
                meta.title_en = title_data.title_en
                meta.title_jp = title_data.title_jp
                meta.title_an = title_data.title_an
                meta.description = title_data.description
                meta.tags = "/".join([str(t) for t in title_data.tags])
                meta.genres = "/".join([str(g) for g in title_data.genres])

                session.add(meta)

                await session.commit()

            except Exception as e:
                print(e)
                await session.rollback()
                raise HTTPException(500)

    except Exception as e:
        print(e)
        raise HTTPException(500)


@router.post("/{id}/cover/{cover_id}")
async def post_title_cover(
    id: int,
    cover_id: int,
    file: UploadFile = File(...),
    user: User = Depends(get_moder),
    session: AsyncSession = Depends(get_session),
):
    if file.content_type is None:
        raise HTTPException(415, "no file supplied")
    if not file.content_type.startswith("image/"):
        raise HTTPException(415, "file is not an image")

    query = select(TitleCover).where(TitleCover.title_id == id, TitleCover.order == cover_id)

    async with session:
        try:
            content = await file.read()
            cover = (await session.execute(query)).scalar_one_or_none()
            if cover is None:
                cover = TitleCover(
                    title_id=id,
                    order=cover_id,
                    data=content,
                )
                cover.approved = True
                session.add(cover)
            else:
                cover.data = content

            await session.commit()

        except Exception as e:
            print("\n\n\n", e, "\n\n\n")
            await session.rollback()
            raise HTTPException(500)


class ratePostScheme(BaseModel):
    rate: int


@router.post("/{id}/rate")
async def rate_title(
    id: int,
    rate: ratePostScheme,
    session: AsyncSession = Depends(get_session),
    user: User = Depends(get_user),
):
    query = select(TitleRate).where(
        TitleRate.title_id == id,
        TitleRate.user_uuid == user.uuid,
    )

    async with session:
        try:
            trate = (await session.execute(query)).scalar_one_or_none()

            if trate is None:
                trate = TitleRate(title_id=id, user_uuid=user.uuid, rating=rate.rate)
                session.add(trate)
            else:
                if trate.rating == rate.rate:
                    await session.delete(trate)
                else:
                    trate.rating = rate.rate

            await session.commit()

        except HTTPException as e:
            await session.rollback()
            raise e

        except Exception as e:
            print(e)
            await session.rollback()
            raise HTTPException(500)


@router.post("/{id}/view")
async def view_title(
    id: int,
    session: AsyncSession = Depends(get_session),
    user: User = Depends(get_user),
):
    query = select(Title).where(Title.id == id)
    view_query = select(TitleView).where(
        TitleView.title_id == id,
        TitleView.user_uuid == user.uuid,
    )

    async with session:
        try:
            title = (await session.execute(query)).scalar_one_or_none()
            if title is None:
                raise HTTPException(404)
            view = (await session.execute(view_query)).scalar_one_or_none()

            if view is None:
                view = TitleView(id, user.uuid)
                session.add(view)
                await session.commit()

        except HTTPException as e:
            await session.rollback()
            raise e

        except Exception as e:
            print(e)
            await session.rollback()
            raise HTTPException(500)
