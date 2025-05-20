from fastapi import APIRouter, Depends, HTTPException

from models.user.user import User
from modules.auth import get_admin
from modules.permission.roles import Role
from services.user.user import UserService
from typealias.notification import NotificationTypeEnum, UserNotificationTypeEnum


router = APIRouter()


@router.post("/role/set/{uuid}/muted")
async def post_set_role_muted(
    uuid: str,
    password: str,
    user: User = Depends(get_admin),
):
    if not UserService(user).password_matches(password=password):
        raise HTTPException(403)

    victim = await UserService.get_by_uuid(uuid=uuid)
    if victim is None:
        raise HTTPException(404)

    ser = UserService(user=victim)

    await ser.set_role(role=Role.muted.value)
    await ser.notify(
        description="Ваша роль была изменена на: заглушен",
        notification_type=NotificationTypeEnum.USER,
        user_notification_type=UserNotificationTypeEnum.ROLE_CHANGED,
        user_uuid=user.uuid,
    )


@router.post("/role/set/{uuid}/default")
async def post_set_role_default(
    uuid: str,
    password: str,
    user: User = Depends(get_admin),
):
    if not UserService(user).password_matches(password=password):
        raise HTTPException(403)

    victim = await UserService.get_by_uuid(uuid=uuid)
    if victim is None:
        raise HTTPException(404)

    ser = UserService(user=victim)

    await ser.set_role(role=Role.default.value)
    await ser.notify(
        description="Ваша роль была изменена на стандартную",
        notification_type=NotificationTypeEnum.USER,
        user_notification_type=UserNotificationTypeEnum.ROLE_CHANGED,
        user_uuid=user.uuid,
    )


@router.post("/role/set/{uuid}/moder")
async def post_set_role_moderator(
    uuid: str,
    password: str,
    user: User = Depends(get_admin),
):
    if not UserService(user).password_matches(password=password):
        raise HTTPException(403)

    victim = await UserService.get_by_uuid(uuid=uuid)
    if victim is None:
        raise HTTPException(404)

    ser = UserService(user=victim)

    await ser.set_role(role=Role.moderator.value)
    await ser.notify(
        description="Ваша роль была изменена на: Модератор",
        notification_type=NotificationTypeEnum.USER,
        user_notification_type=UserNotificationTypeEnum.ROLE_CHANGED,
        user_uuid=user.uuid,
    )


@router.post("/role/set/{uuid}/admin")
async def post_set_role_admin(
    uuid: str,
    password: str,
    user: User = Depends(get_admin),
):
    if not UserService(user).password_matches(password=password):
        raise HTTPException(403)

    victim = await UserService.get_by_uuid(uuid=uuid)
    if victim is None:
        raise HTTPException(404)

    ser = UserService(user=victim)

    await ser.set_role(role=Role.admin.value)
    await ser.notify(
        description="Ваша роль была изменена на: Админ",
        notification_type=NotificationTypeEnum.USER,
        user_notification_type=UserNotificationTypeEnum.ROLE_CHANGED,
        user_uuid=user.uuid,
    )


@router.delete("/user/{uuid}")
async def delete_user(
    uuid: str,
    password: str,
    user: User = Depends(get_admin),
):
    if not UserService(user).password_matches(password=password):
        raise HTTPException(403)

    victim = await UserService.get_by_uuid(uuid=uuid)
    if victim is None:
        raise HTTPException(404)

    ser = UserService(user=victim)
    await ser.delete()
