from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.tags import Tag, Genre
from schemas.tag import TagScheme
from db.session_fabric import get_session

router = APIRouter()


@router.get("/tags")
async def get_tags(session: AsyncSession = Depends(get_session)) -> list[TagScheme]:
    exec = await session.execute(select(Tag))
    return [TagScheme(id=t.id, ru=t.ru, en=t.en) for t in exec.scalars().all()]


@router.get("/genres")
async def get_genres(session: AsyncSession = Depends(get_session)) -> list[TagScheme]:
    exec = await session.execute(select(Genre))
    return [TagScheme(id=t.id, ru=t.ru, en=t.en) for t in exec.scalars().all()]
