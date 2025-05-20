from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.types import HTTPExceptionHandler

from db.session_fabric import get_session
from models.title.meta import TitleMeta
from models.user.user import User
from modules.auth import get_moder
from modules.permission.roles import Role
from schemas.title import TitleMetaScheme, TitlesMetaSchemes
from services.title.meta import TitleMetaService
from services.user.moder import ModerService
from services.user.user import UserService
from typealias.notification import NotificationTypeEnum, UserNotificationTypeEnum


router = APIRouter()


@router.get("/title/meta/pending")
async def titles_get_pending_meta(
    user: User = Depends(get_moder),
    session: AsyncSession = Depends(get_session),
) -> list[TitleMetaScheme]:
    exec = await session.execute(select(TitleMeta).where(TitleMeta.approved == False))
    metas = exec.scalars().all()
    return [TitleMetaService(meta).to_scheme() for meta in metas]


@router.get("/title/{id}/meta/pending")
async def title_get_pending_meta(
    id: int,
    user: User = Depends(get_moder),
    session: AsyncSession = Depends(get_session),
) -> list[TitleMetaScheme]:
    exec = await session.execute(
        select(TitleMeta).where(TitleMeta.approved == False, TitleMeta.title_id == id)
    )
    metas = exec.scalars().all()
    return [TitleMetaService(meta).to_scheme() for meta in metas]


@router.post("/{uuid}/mute")
async def post_mute(uuid: str, user: User = Depends(get_moder)):
    victim = await UserService.get_by_uuid(uuid=uuid)
    if victim is None:
        raise HTTPException(404)

    ser = UserService(user=victim)

    if not ser.role_is_default():
        raise HTTPException(403)

    await ser.set_role(role=Role.muted.value)
    await ser.notify(
        description="Вы были замучены",
        notification_type=NotificationTypeEnum.USER,
        user_notification_type=UserNotificationTypeEnum.ROLE_CHANGED,
        user_uuid=user.uuid,
    )


@router.post("/{uuid}/unmute")
async def post_unmute(uuid: str, user: User = Depends(get_moder)):
    victim = await UserService.get_by_uuid(uuid=uuid)
    if victim is None:
        raise HTTPException(404)

    ser = UserService(user=victim)

    if not ser.role_is_muted():
        raise HTTPException(403)

    await ser.set_role(role=Role.default.value)
    await ser.notify(
        description="Вы были размучены",
        notification_type=NotificationTypeEnum.USER,
        user_notification_type=UserNotificationTypeEnum.ROLE_CHANGED,
        user_uuid=user.uuid,
    )


@router.delete("/meta/{id}/decline")
async def title_decline_meta(
    id: int,
    user: User = Depends(get_moder),
):
    meta = await TitleMetaService.get_by_id(id=id)
    if meta is None:
        raise HTTPException(404)
    mod = ModerService(user=user)
    await mod.decline_meta(meta=meta)


@router.post("/meta/{id}/approve")
async def title_approve_meta(
    id: int,
    user: User = Depends(get_moder),
):
    meta = await TitleMetaService.get_by_id(id=id)
    if meta is None:
        raise HTTPException(404)
    mod = ModerService(user=user)
    await mod.approve_meta(meta=meta)
