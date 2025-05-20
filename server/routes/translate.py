from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.session_fabric import get_session
from models.user.user import User
from modules.auth import get_not_muted
from schemas.translate import TranslateTeamPostScheme


router = APIRouter()


@router.post("/create")
async def create_translate_team(
    scheme: TranslateTeamPostScheme,
    user: User = Depends(get_not_muted),
    session: AsyncSession = Depends(get_session),
):
    pass
