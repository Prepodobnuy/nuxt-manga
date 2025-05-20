from dataclasses import dataclass

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.session_fabric import connection
from models.title.title import Title
from models.user.user import User


@dataclass
class TitleService:
    title: Title

    @staticmethod
    @connection
    async def get_by_id(
        id: int,
        session: AsyncSession | None = None,
    ) -> Title | None:
        assert session is not None

        exec = await session.execute(select(Title).where(Title.id == id))
        return exec.scalar_one_or_none()

    @staticmethod
    def create(user: User) -> Title:
        return Title(created_user_uuid=user.uuid)
