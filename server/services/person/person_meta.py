from dataclasses import dataclass
from datetime import datetime, timezone

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.session_fabric import connection
from models.person.person import Person
from models.person.personmeta import PersonMeta
from models.user import User
from schemas.person import PersonMetaPostScheme, PersonMetaScheme, PersonScheme


@dataclass
class PersonMetaService:
    meta: PersonMeta

    @staticmethod
    def create(
        user: User,
        person: Person,
        name_ru: str,
        name_en: str,
        name_jp: str,
        name_an: str | None,
        description: str | None,
        session: AsyncSession | None = None,
    ) -> PersonMeta:
        meta = PersonMeta(
            person_id=person.id,
            created_user_uuid=user.uuid,
            name_ru=name_ru,
            name_en=name_en,
            name_jp=name_jp,
            name_an=name_an,
            description=description,
        )

        return meta

    @connection
    @staticmethod
    async def get_by_id(
        id: int,
        session: AsyncSession | None = None,
    ) -> PersonMeta | None:
        assert session is not None

        exec = await session.execute(select(PersonMeta).where(PersonMeta.id == id))

        return exec.scalar_one_or_none()

    @connection
    async def delete(
        self,
        session: AsyncSession | None = None,
    ):
        assert session is not None

        await session.delete(self.meta)
        await session.commit()

    @staticmethod
    def create_from_scheme(
        user: User,
        person: Person,
        scheme: PersonMetaPostScheme,
    ) -> PersonMeta:
        meta = PersonMetaService.create(
            user=user,
            person=person,
            name_ru=scheme.name_ru,
            name_en=scheme.name_en,
            name_jp=scheme.name_jp,
            name_an=scheme.name_an,
            description=scheme.description,
        )

        return meta

    @connection
    async def approve(
        self,
        user: User,
        session: AsyncSession | None = None,
    ):
        assert session is not None

        self.meta.approved = True
        self.meta.approved_at = datetime.now(timezone.utc)
        self.meta.approved_user_uuid = user.uuid

        await session.commit()

    @connection
    async def disapprove(
        self,
        session: AsyncSession | None = None,
    ):
        assert session is not None

        self.meta.approved = False

        await session.commit()

    def to_scheme(
        self,
    ) -> PersonMetaScheme:
        return PersonMetaScheme(
            id=self.meta.id,
            person_id=self.meta.person_id,
            created_user_uuid=self.meta.created_user_uuid,
            name_ru=self.meta.name_ru,
            name_en=self.meta.name_en,
            name_jp=self.meta.name_jp,
            name_an=self.meta.name_an,
            description=self.meta.description,
            approved=self.meta.approved,
            approved_at=self.meta.approved_at,
            approved_user_uuid=self.meta.approved_user_uuid,
            created_at=self.meta.created_at,
        )
