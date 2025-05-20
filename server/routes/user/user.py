import io

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from fastapi.responses import StreamingResponse

from models.user.user import User
from modules.auth import get_user
from schemas.user import UserScheme
from services.user import UserService
from services.user.asset import UserAssetService


router = APIRouter()


@router.get("/self")
async def get_user_self(user: User = Depends(get_user)) -> UserScheme:
    print("get user")
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
