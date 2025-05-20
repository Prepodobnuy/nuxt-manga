from dataclasses import dataclass
from io import BytesIO
from PIL import Image
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from config.assets import PERSON_COVER_RESOLUTION
from db.session_fabric import connection
from models.assets.person import PersonCover
from models.person.person import Person


@dataclass
class PersonAssetService:
    person: Person

    async def set_cover(
        self,
        data: bytes,
        session: AsyncSession,
    ):
        try:
            byte_io = BytesIO(data)

            with Image.open(byte_io) as img:
                img = img.resize(PERSON_COVER_RESOLUTION)
                output = BytesIO()
                img.save(output, format="PNG")
                processed_data = output.getvalue()

            query = select(PersonCover).where(PersonCover.person_id == self.person.id)
            result = await session.execute(query)
            cover = result.scalar_one_or_none()

            if cover:
                cover.data = processed_data
            else:
                cover = PersonCover(person_id=self.person.id, data=processed_data)
                session.add(cover)

            await session.flush()
        except Exception as e:
            raise ValueError(f"Failed to process cover image: {str(e)}")

    @connection
    async def get_cover(
        self,
        session: AsyncSession | None = None,
    ) -> bytes | None:
        assert session is not None

        query = select(PersonCover).where(PersonCover.person_id == self.person.id)
        exec = await session.execute(query)
        cover = exec.scalar_one_or_none()

        return cover.data if cover else None
