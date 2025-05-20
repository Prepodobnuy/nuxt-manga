from dataclasses import dataclass

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.session_fabric import connection
from models.person.person import Person
from models.person.personmeta import PersonMeta
from models.user import User
from schemas.person import PersonMetaPostScheme, PersonScheme
from services.person.person_meta import PersonMetaService


@dataclass
class PersonService:
    person: Person

    @connection
    @staticmethod
    async def get_by_id(
        id: int,
        session: AsyncSession | None = None,
    ) -> Person | None:
        assert session is not None

        exec = await session.execute(select(Person).where(Person.id == id))

        return exec.scalar_one_or_none()

    @staticmethod
    def create(
        user: User,
    ) -> Person:
        person = Person(user_published_uuid=user.uuid)

        return person

    @connection
    async def delete(
        self,
        session: AsyncSession | None = None,
    ):
        assert session is not None

        metas = await self.get_all_meta()
        for meta in metas:
            await session.delete(meta)
        await session.flush()

        await session.delete(self.person)
        await session.commit()

    @connection
    async def get_all_meta(
        self,
        session: AsyncSession | None = None,
    ) -> list[PersonMeta]:
        assert session is not None

        query = select(PersonMeta).where(
            PersonMeta.person_id == self.person.id,
        )

        exec = await session.execute(query)
        return exec.scalars().all()

    @staticmethod
    def create_from_scheme(
        user: User,
    ) -> Person:
        person = Person(user_published_uuid=user.uuid)
        return person

    @connection
    async def to_scheme(
        self,
        include_unaproved_meta: bool = False,
        session: AsyncSession | None = None,
    ) -> PersonScheme:
        assert session is not None
        approved_meta_query = select(PersonMeta).where(
            PersonMeta.approved == True,
            PersonMeta.person_id == self.person.id,
        )

        unapproved_meta_query = select(PersonMeta).where(
            PersonMeta.approved == False,
            PersonMeta.person_id == self.person.id,
        )

        unapproved_meta = []

        if include_unaproved_meta:
            unapproved_exec = await session.execute(unapproved_meta_query)
            unapproved_meta = unapproved_exec.scalars().all()
        approved_exec = await session.execute(approved_meta_query)

        approved_meta = approved_exec.scalar_one_or_none()

        approved_scheme = None
        if approved_meta is not None:
            approved_scheme = PersonMetaService(approved_meta).to_scheme()

        unapproved_schemas = [PersonMetaService(meta).to_scheme() for meta in unapproved_meta]

        return PersonScheme(
            id=self.person.id,
            user_published_uuid=self.person.user_published_uuid,
            created_at=self.person.created_at,
            meta=approved_scheme,
            unapproved_metas=unapproved_schemas,
        )

    @connection
    @staticmethod
    async def quick_search(
        prompt: str,
        session: AsyncSession | None = None,
    ) -> list[Person]:
        assert session is not None

        query = (
            select(PersonMeta)
            .where(
                PersonMeta.approved == True,
                PersonMeta.name_ru.ilike(f"%{prompt}%")
                | PersonMeta.name_en.ilike(f"%{prompt}%")
                | PersonMeta.name_jp.ilike(f"%{prompt}%")
                | PersonMeta.name_an.ilike(f"%{prompt}%"),
            )
            .limit(10)
        )

        exec = await session.execute(query)

        res = []
        for m in exec.scalars().all():
            res.append(await PersonService.get_by_id(m.person_id))

        return res

    @connection
    @staticmethod
    async def get_unaproved(
        session: AsyncSession | None = None,
    ) -> list[Person]:
        assert session is not None

        query = select(PersonMeta).where(
            PersonMeta.approved == False,
        )

        exec = await session.execute(query)

        res = []
        for m in exec.scalars().all():
            res.append(await PersonService.get_by_id(m.person_id))

        return res
