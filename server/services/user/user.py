from hashlib import md5
from dataclasses import dataclass
import re

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from config.assets import FHD_DIVIDER, HD_DIVIDER, SD_DIVIDER, USER_PFP_RESOLUTION
from db.session_fabric import connection
from models.notification import Notification
from models.translate.translate_team import TranslateTeam
from models.translate.translate_team_member import TranslateTeamMember
from models.user.user import User
from modules.permission import roles
from modules.permission.roles import Role
from schemas.user import UserScheme
from services.asset import AssetService
from typealias.notification import (
    CommentNotificationTypeEnum,
    NotificationTypeEnum,
    PageNotificationTypeEnum,
    ReportNotificationTypeEnum,
    TitleNotificationTypeEnum,
    UserNotificationTypeEnum,
)


def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None


@dataclass
class UserService:
    user: User

    def password_matches(self, password: str) -> bool:
        return UserService.hash_password(password) == self.user.hashed_password

    def role_is_muted(self) -> bool:
        return self.user.role == Role.muted.value

    def role_is_default(self) -> bool:
        return self.user.role == Role.default.value

    def role_is_moderator(self) -> bool:
        return self.user.role == Role.moderator.value

    def role_is_admin(self) -> bool:
        return self.user.role == Role.admin.value

    @staticmethod
    @connection
    async def validate_username(
        username: str,
        session: AsyncSession | None = None,
    ):
        assert session is not None
        if len(username) < 4:
            raise HTTPException(400, "username too short")
        if len(username) > 20:
            raise HTTPException(400, "username too long")
        if await UserService.get_by_username(username=username) is not None:
            raise HTTPException(400, "username taken")

    @staticmethod
    @connection
    async def validate_nickname(
        nickname: str,
        session: AsyncSession | None = None,
    ):
        assert session is not None
        if len(nickname) < 4:
            raise HTTPException(400, "nickname too short")
        if len(nickname) > 20:
            raise HTTPException(400, "nickname too long")

    @staticmethod
    @connection
    async def validate_email(
        email: str,
        session: AsyncSession | None = None,
    ):
        assert session is not None
        if not is_valid_email(email=email):
            raise HTTPException(400, "email invalid")
        if await UserService.get_by_email(email=email) is not None:
            raise HTTPException(400, "email taken")

    @staticmethod
    @connection
    async def validate_password(
        password: str,
        session: AsyncSession | None = None,
    ):
        assert session is not None
        if len(password) < 9:
            raise HTTPException(400, "password too short")
        if len(password) > 30:
            raise HTTPException(400, "password too long")

    @connection
    async def notify(
        self,
        description: str,
        notification_type: NotificationTypeEnum,
        user_notification_type: UserNotificationTypeEnum | None = None,
        page_notification_type: PageNotificationTypeEnum | None = None,
        report_notification_type: ReportNotificationTypeEnum | None = None,
        comment_notification_type: CommentNotificationTypeEnum | None = None,
        title_notification_type: TitleNotificationTypeEnum | None = None,
        user_uuid: str | None = None,
        comment_id: int | None = None,
        title_id: int | None = None,
        page_id: int | None = None,
        report_id: int | None = None,
        session: AsyncSession | None = None,
    ):
        assert session is not None

        notification = Notification(
            target_user_uuid=self.user.uuid,
            description=description,
            notification_type=notification_type,
            user_notification_type=user_notification_type,
            page_notification_type=page_notification_type,
            report_notification_type=report_notification_type,
            comment_notification_type=comment_notification_type,
            title_notification_type=title_notification_type,
            user_uuid=user_uuid,
            comment_id=comment_id,
            title_id=title_id,
            page_id=page_id,
            report_id=report_id,
        )

        session.add(notification)
        await session.commit()

    @connection
    async def set_role(
        self,
        role: str,
        session: AsyncSession | None = None,
    ):
        assert session is not None
        self.user.role = role
        await session.commit()

    def set_pfp(self, bytes: bytes):
        fhd = AssetService(["user", self.user.uuid, "pfp"], "fhd")
        hd = AssetService(["user", self.user.uuid, "pfp"], "hd")
        sd = AssetService(["user", self.user.uuid, "pfp"], "sd")

        geometry = USER_PFP_RESOLUTION

        fhd_geometry = (
            int(geometry[0] / FHD_DIVIDER),
            int(geometry[1] / FHD_DIVIDER),
        )
        hd_geometry = (
            int(geometry[0] / HD_DIVIDER),
            int(geometry[1] / HD_DIVIDER),
        )
        sd_geometry = (
            int(geometry[0] / SD_DIVIDER),
            int(geometry[1] / SD_DIVIDER),
        )

        fhd.set(geometry=fhd_geometry, bytes=bytes)
        hd.set(geometry=hd_geometry, bytes=bytes)
        sd.set(geometry=sd_geometry, bytes=bytes)

    def get_pfp(self) -> bytes | None:
        fhd = AssetService(["user", self.user.uuid, "pfp"], "fhd")
        return fhd.get()

    @staticmethod
    @connection
    async def get_by_uuid(
        uuid: str,
        session: AsyncSession | None = None,
    ) -> User | None:
        assert session is not None
        exec = await session.execute(select(User).where(User.uuid == uuid))
        return exec.scalar_one_or_none()

    @staticmethod
    @connection
    async def get_by_username(
        username: str,
        session: AsyncSession | None = None,
    ) -> User | None:
        assert session is not None
        exec = await session.execute(select(User).where(User.username == username))
        return exec.scalar_one_or_none()

    @staticmethod
    @connection
    async def get_by_email(
        email: str,
        session: AsyncSession | None = None,
    ) -> User | None:
        assert session is not None
        exec = await session.execute(select(User).where(User.email == email))
        return exec.scalar_one_or_none()

    @staticmethod
    @connection
    async def get_by_nickname(
        nickname: str,
        session: AsyncSession | None = None,
    ) -> list[User]:
        assert session is not None
        res = []
        exec = await session.execute(select(User).where(User.nickname == nickname))
        for user in exec.scalars():
            res.append(user)
        return res

    @connection
    async def delete(self, session: AsyncSession | None = None):
        assert session is not None
        await session.delete(self.user)
        await session.commit()

    @staticmethod
    def hash_password(password: str) -> str:
        return md5(password.encode()).hexdigest()

    @connection
    async def to_scheme(self, session: AsyncSession | None = None) -> UserScheme:
        assert session is not None

        muted = self.user.role == Role.muted.value
        admin = self.user.role == Role.admin.value
        moder = self.user.role == Role.moderator.value

        exec = await session.execute(select(TranslateTeamMember).where(TranslateTeamMember.uuid==self.user.uuid))
        sexec = await session.execute(select(TranslateTeam).where(TranslateTeam.owner_uuid==self.user.uuid))

        translator = exec.first() is not None or sexec.first() is not None

        return UserScheme(
            uuid=self.user.uuid,
            role=self.user.role,
            username=self.user.username,
            email=self.user.email,
            nickname=self.user.nickname,
            status=self.user.status,
            about=self.user.about,
            created_at=self.user.created_at,
            muted=muted,
            admin=admin,
            moder=moder,
            translator=translator,
        )

    @connection
    async def set_username(
        self,
        username: str,
        session: AsyncSession | None = None,
    ):
        assert session is not None
        await UserService.validate_username(username=username)

        self.user.username = username
        await session.commit()

    @connection
    async def set_email(
        self,
        email: str,
        session: AsyncSession | None = None,
    ):
        assert session is not None
        await UserService.validate_email(email=email)

        self.user.email = email
        await session.commit()

    @connection
    async def set_password(
        self,
        password: str,
        session: AsyncSession | None = None,
    ):
        assert session is not None
        await UserService.validate_password(password=password)

        self.user.hashed_password = UserService.hash_password(password)
        await session.commit()

    @connection
    async def set_nickname(
        self,
        nickname: str,
        session: AsyncSession | None = None,
    ):
        assert session is not None
        await UserService.validate_nickname(nickname=nickname)

        self.user.nickname = nickname
        await session.commit()

    @connection
    async def set_status(
        self,
        status: str | None,
        session: AsyncSession | None = None,
    ):
        assert session is not None

        self.user.status = status
        await session.commit()

    @connection
    async def set_about(
        self,
        about: str | None,
        session: AsyncSession | None = None,
    ):
        assert session is not None

        self.user.about = about
        await session.commit()

    @staticmethod
    @connection
    async def create(
        username: str,
        email: str,
        password: str,
        nickname: str,
        about: str | None = None,
        status: str | None = None,
        session: AsyncSession | None = None,
    ) -> User:
        assert session is not None

        await UserService.validate_email(email=email)
        await UserService.validate_username(username=username)
        await UserService.validate_nickname(nickname=nickname)
        await UserService.validate_password(password=password)

        if len(nickname) < 4:
            raise HTTPException(400, "nickname too short")
        if len(nickname) > 20:
            raise HTTPException(400, "nickname too long")

        user = User(
            username=username,
            email=email,
            hashed_password=UserService.hash_password(password),
            nickname=nickname,
            about=about,
            status=status,
        )
        session.add(user)
        await session.commit()
        return user
