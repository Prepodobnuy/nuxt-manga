from dataclasses import dataclass
from datetime import datetime, timezone

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession


from db.session_fabric import connection
from models.title.meta import TitleMeta
from models.title.title import Title
from models.user.user import User
from schemas.title import TitleMetaPostScheme, TitleMetaScheme
from services.user.user import UserService
from typealias.notification import (
    NotificationTypeEnum,
    TitleNotificationTypeEnum,
)


@dataclass
class TitleMetaService:
    meta: TitleMeta

    @staticmethod
    def create(
        title: Title,
        user: User,
        title_ru: str,
        title_en: str,
        title_jp: str,
        title_an: str | None,
        description: str | None,
        author_id: int,
        artist_id: int,
        publisher_id: int,
        tags: str,
        genres: str,
    ) -> TitleMeta:
        return TitleMeta(
            title_id=title.id,
            created_user_uuid=user.uuid,
            title_ru=title_ru,
            title_en=title_en,
            title_jp=title_jp,
            title_an=title_an,
            description=description,
            author_id=author_id,
            artist_id=artist_id,
            publisher_id=publisher_id,
            tags=tags,
            genres=genres,
        )

    @staticmethod
    def create_from_scheme(title: Title, user: User, scheme: TitleMetaPostScheme) -> TitleMeta:
        return TitleMetaService.create(
            title=title,
            user=user,
            title_ru=scheme.title_ru,
            title_en=scheme.title_en,
            title_jp=scheme.title_jp,
            title_an=scheme.title_an,
            description=scheme.description,
            author_id=scheme.author_id,
            artist_id=scheme.artist_id,
            publisher_id=scheme.publisher_id,
            tags="/".join([str(t) for t in scheme.tags]),
            genres="/".join([str(g) for g in scheme.genres]),
        )

    def to_scheme(self) -> TitleMetaScheme:
        return TitleMetaScheme(
            id=self.meta.id,
            title_id=self.meta.title_id,
            title_ru=self.meta.title_ru,
            title_en=self.meta.title_en,
            title_jp=self.meta.title_jp,
            title_an=self.meta.title_an,
            description=self.meta.description,
            author_id=self.meta.author_id,
            artist_id=self.meta.artist_id,
            publisher_id=self.meta.publisher_id,
            tags=[int(t) for t in self.meta.tags.split("/")] if self.meta.tags is not None else [],
            genres=[int(t) for t in self.meta.genres.split("/")]
            if self.meta.genres is not None
            else [],
            approved=self.meta.approved,
            approved_at=self.meta.approved_at,
            approved_user_uuid=self.meta.approved_user_uuid,
            created_user_uuid=self.meta.created_user_uuid,
            created_at=self.meta.created_at,
        )

    @staticmethod
    @connection
    async def get_by_id(
        id: int,
        session: AsyncSession | None = None,
    ) -> TitleMeta | None:
        assert session is not None

        exec = await session.execute(select(TitleMeta).where(TitleMeta.id == id))
        return exec.scalar_one_or_none()

    @staticmethod
    @connection
    async def get_by_title(
        title: Title,
        session: AsyncSession | None = None,
    ) -> TitleMeta | None:
        assert session is not None

        exec = await session.execute(select(TitleMeta).where(TitleMeta.title_id == title.id))
        return exec.scalar_one_or_none()

    @connection
    async def decline(
        self,
        user: User,
        session: AsyncSession | None = None,
    ):
        assert session is not None

        await session.delete(self.meta)

        exec = await session.execute(select(User).where(User.uuid == self.meta.created_user_uuid))
        tuser = exec.scalar_one_or_none()
        if tuser is not None:
            ser = UserService(user=tuser)
            await ser.notify(
                description="Ваше предложение по изменению информации о тайтле было отклонено",
                notification_type=NotificationTypeEnum.TITLE,
                title_notification_type=TitleNotificationTypeEnum.META_ACCEPTED,
                title_id=self.meta.title_id,
            )

        await session.commit()

    @connection
    async def approve(
        self,
        user: User,
        session: AsyncSession | None = None,
    ):
        assert session is not None

        await session.execute(
            delete(TitleMeta).where(
                TitleMeta.title_id == self.meta.title_id,
                TitleMeta.approved == True,
            )
        )
        self.meta.approved = True
        self.meta.approved_at = datetime.now(timezone.utc)
        self.meta.approved_user_uuid = user.uuid

        exec = await session.execute(select(User).where(User.uuid == self.meta.created_user_uuid))
        tuser = exec.scalar_one_or_none()
        if tuser is not None:
            ser = UserService(user=tuser)
            await ser.notify(
                description="Ваше предложение по изменению информации о тайтле было принято!",
                notification_type=NotificationTypeEnum.TITLE,
                title_notification_type=TitleNotificationTypeEnum.META_ACCEPTED,
                title_id=self.meta.title_id,
            )

        await session.commit()
