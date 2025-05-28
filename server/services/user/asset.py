from dataclasses import dataclass
from io import BytesIO

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.session_fabric import connection
from models.assets.user import UserBack, UserPfp
from models.user.user import User

from PIL import Image
from config.assets import USER_PFP_RESOLUTION, USER_BACK_RESOLUTION


@dataclass
class UserAssetService:
    user: User

    @connection
    async def get_pfp(
        self,
        session: AsyncSession | None = None,
    ) -> bytes | None:
        assert session is not None

        query = select(UserPfp).where(UserPfp.uuid == self.user.uuid)
        exec = await session.execute(query)
        pfp = exec.scalar_one_or_none()
        if pfp is None:
            return None

        return pfp.data

    @connection
    async def set_pfp(
        self,
        data: bytes,
        session: AsyncSession | None = None,
    ):
        assert session is not None

        query = select(UserPfp).where(UserPfp.uuid == self.user.uuid)
        exec = await session.execute(query)
        pfp = exec.scalar_one_or_none()

        if pfp is not None:
            pfp.data = data
        else:
            pfp = UserPfp(uuid=self.user.uuid, data=data)
            session.add(pfp)

        await session.commit()

    @connection
    async def get_back(
        self,
        session: AsyncSession | None = None,
    ) -> bytes | None:
        assert session is not None

        query = select(UserBack).where(UserBack.uuid == self.user.uuid)
        exec = await session.execute(query)
        back = exec.scalar_one_or_none()
        if back is None:
            return None

        return back.data

    @connection
    async def set_back(
        self,
        data: bytes,
        session: AsyncSession | None = None,
    ):
        assert session is not None

        query = select(UserBack).where(UserBack.uuid == self.user.uuid)
        exec = await session.execute(query)
        back = exec.scalar_one_or_none()

        if back is not None:
            back.data = data
        else:
            back = UserBack(uuid=self.user.uuid, data=data)
            session.add(back)

        await session.commit()

    @connection
    async def delete(
        self,
        session: AsyncSession | None = None,
    ):
        assert session is not None

        query = select(UserPfp).where(UserPfp.uuid == self.user.uuid)
        exec = await session.execute(query)
        pfp = exec.scalar_one_or_none()

        query = select(UserBack).where(UserBack.uuid == self.user.uuid)
        exec = await session.execute(query)
        back = exec.scalar_one_or_none()

        if back is not None:
            await session.delete(back)

        if pfp is not None:
            await session.delete(pfp)

        if back is not None or pfp is not None:
            await session.commit()
