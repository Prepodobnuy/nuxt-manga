from dataclasses import dataclass
from io import BytesIO
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from config.assets import TITLE_COVER_RESOLUTION
from db.session_fabric import connection
from models.assets.title import TitleCover
from models.title import Title

from PIL import Image

from schemas.title import TitleCoverScheme


@dataclass
class TitleAssetService:
    title: Title

    @connection
    async def list_covers(
        self,
        session: AsyncSession | None = None,
    ) -> list[TitleCoverScheme]:
        assert session is not None

        query = select(TitleCover).where(TitleCover.title_id == self.title.id)
        exec = await session.execute(query)
        covers = exec.scalars().all()

        return [TitleCoverScheme(id=c.id, title_id=c.title_id, order=c.order) for c in covers]

    async def set_cover(
        self,
        data: bytes,
        order: int,
        session: AsyncSession,
    ):
        order = min(max(order, 0), 9)

        try:
            byte_io = BytesIO(data)

            with Image.open(byte_io) as img:
                img = img.resize(TITLE_COVER_RESOLUTION)
                output = BytesIO()
                img.save(output, format="PNG")
                processed_data = output.getvalue()

            query = select(TitleCover).where(
                TitleCover.title_id == self.title.id, TitleCover.order == order
            )
            result = await session.execute(query)
            cover = result.scalar_one_or_none()

            if cover:
                cover.data = processed_data
            else:
                cover = TitleCover(title_id=self.title.id, data=processed_data, order=order)
                session.add(cover)

            await session.flush()
        except Exception as e:
            raise ValueError(f"Failed to process cover image: {str(e)}")

    @connection
    async def get_cover(
        self,
        order: int,
        session: AsyncSession | None = None,
    ) -> bytes | None:
        assert session is not None
        order = min(max(order, 0), 9)

        query = select(TitleCover).where(
            TitleCover.title_id == self.title.id, TitleCover.order == order
        )
        exec = await session.execute(query)
        cover = exec.scalar_one_or_none()
        if cover is None:
            return None

        return cover.data

    @connection
    async def get_first_cover(
        self,
        session: AsyncSession | None = None,
    ) -> bytes | None:
        assert session is not None

        query = select(TitleCover).where(TitleCover.title_id == self.title.id)
        exec = await session.execute(query)
        cover = exec.scalar_one_or_none()
        if cover is None:
            return None

        return cover.data
