import io

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from fastapi.responses import StreamingResponse
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.session_fabric import get_session
from models.user.user import User
from modules.auth import get_user
from schemas.person import PersonScheme
from schemas.user import UserScheme
from services.user import UserService
from services.user.asset import UserAssetService


router = APIRouter()


@router.get("/search/{prompt}")
async def quick_search(
    prompt: str,
    session: AsyncSession = Depends(get_session),
) -> list[UserScheme]:
    async with session:
        query = (
            select(User)
            .where(
                User.username.ilike(f"%{prompt}%")
                | User.nickname.ilike(f"%{prompt}%")
                | User.email.ilike(f"%{prompt}%")
            )
            .limit(10)
        )

        exec = await session.execute(query)

        res = []
        for m in exec.scalars().all():
            res.append((await UserService(user=m).to_scheme()))

        return res


@router.get("/self")
async def get_user_self(user: User = Depends(get_user)) -> UserScheme:
    return await UserService(user=user).to_scheme()


@router.get("/{uuid}")
async def get_user_default(uuid: str) -> UserScheme:
    user = await UserService.get_by_uuid(uuid=uuid)
    if user is None:
        raise HTTPException(404)

    return await UserService(user=user).to_scheme()


@router.delete("/self")
async def delete_user_self(password: str, user: User = Depends(get_user)):
    ser = UserService(user)

    if not ser.password_matches(password=password):
        raise HTTPException(403, "password does not match")

    await ser.delete()
