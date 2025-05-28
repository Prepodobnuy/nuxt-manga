from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy import except_, select
from sqlalchemy.ext.asyncio import AsyncSession

from db.session_fabric import get_session
from models.page.asset import PageAsset
from models.page.page import Page
from models.translate.translate_team import TranslateTeam
from models.user.user import User
from modules.auth import get_user
from schemas.page import PagePostScheme, PageScheme


router = APIRouter()


async def _user_can_add_pages(
    user: User,
    session: AsyncSession,
) -> bool:
    query = select(TranslateTeam).where(
        TranslateTeam.approved == True,
        TranslateTeam.owner_uuid == user.uuid,
    )

    return (await session.execute(query)).scalar_one_or_none() is not None


async def _get_page(
    id: int,
    session: AsyncSession,
) -> Page | None:
    query = select(Page).where(Page.id == id)

    return (await session.execute(query)).scalar_one_or_none()


async def _get_page_asset(
    id: int,
    session: AsyncSession,
) -> PageAsset | None:
    query = select(PageAsset).where(PageAsset.page_id == id)

    return (await session.execute(query)).scalar_one_or_none()


@router.get("/title/{id}/pages")
async def get_title_pages(
    id: int, session: AsyncSession = Depends(get_session)
) -> list[PageScheme]:
    query = select(Page).where(
        Page.title_id == id,
    )

    pages = (await session.execute(query)).scalars().all()
    return [
        PageScheme(
            id=p.id,
            volume=p.volume,
            chapter=p.chapter,
            order=p.order,
        )
        for p in pages
    ]


@router.post("/title/{id}/")
async def post_page_meta(
    id: int,
    scheme: PagePostScheme,
    user: User = Depends(get_user),
    session: AsyncSession = Depends(get_session),
):
    if not await _user_can_add_pages(user, session):
        raise HTTPException(403)

    async with session:
        try:
            page = Page(
                title_id=id,
                user_uuid=user.uuid,
                volume=scheme.volume,
                chapter=scheme.chapter,
                order=scheme.order,
            )

            session.add(page)
            await session.commit()

        except Exception as e:
            await session.rollback()
            raise HTTPException(500)

    pass


@router.post("/{id}/asset")
async def put_page_asset(
    id: int,
    file: UploadFile = File(...),
    user: User = Depends(get_user),
    session: AsyncSession = Depends(get_session),
):
    if not await _user_can_add_pages(user, session):
        raise HTTPException(403)

    if file.content_type is None:
        raise HTTPException(415, "no file supplied")
    if not file.content_type.startswith("image/"):
        raise HTTPException(415, "file is not an image")

    page = await _get_page(id, session)
    asset = await _get_page_asset(id, session)
    if page is None:
        raise HTTPException(404)

    async with session:
        try:
            data = await file.read()

            if asset is None:
                asset = PageAsset(page_id=page.id, content=data)
                session.add(asset)
            else:
                asset.content = data

            await session.commit()
        except Exception as e:
            await session.rollback()
            raise HTTPException(500)


@router.put("/{id}")
async def put_page_meta(
    id: int,
    scheme: PagePostScheme,
    user: User = Depends(get_user),
    session: AsyncSession = Depends(get_session),
):
    if not await _user_can_add_pages(user, session):
        raise HTTPException(403)

    page = await _get_page(id, session)
    if page is None:
        raise HTTPException(404)

    async with session:
        try:
            page.volume = scheme.volume
            page.chapter = scheme.chapter
            page.order = scheme.order
            await session.commit()
        except Exception as e:
            await session.rollback()
            raise HTTPException(500)


@router.delete("/{id}")
async def delete_page_meta(
    id: int,
    user: User = Depends(get_user),
    session: AsyncSession = Depends(get_session),
):
    if not await _user_can_add_pages(user, session):
        raise HTTPException(403)

    page = await _get_page(id, session)
    asset = await _get_page_asset(id, session)
    if page is None:
        raise HTTPException(404)

    async with session:
        try:
            if asset is not None:
                await session.delete(asset)
                await session.flush()

            await session.delete(page)
            await session.commit()
        except Exception as e:
            await session.rollback()
            raise HTTPException(500)
