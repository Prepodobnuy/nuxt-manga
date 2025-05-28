import io

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from fastapi.responses import StreamingResponse
from sqlalchemy.ext.asyncio import AsyncSession

from db.session_fabric import get_session
from models.user.user import User
from modules.auth import get_user
from schemas.user import UserScheme
from services.user import UserService
from services.user.asset import UserAssetService


router = APIRouter()


@router.post("/pfp")
async def put_user_pfp(
    file: UploadFile = File(...),
    user: User = Depends(get_user),
):
    ser = UserAssetService(user=user)

    if file.content_type is None:
        raise HTTPException(415, "no file supplied")
    if not file.content_type.startswith("image/"):
        raise HTTPException(415, "file is not an image")

    content = await file.read()
    await ser.set_pfp(data=content)


@router.post("/back")
async def put_user_back(
    file: UploadFile = File(...),
    user: User = Depends(get_user),
):
    ser = UserAssetService(user=user)

    if file.content_type is None:
        raise HTTPException(415, "no file supplied")
    if not file.content_type.startswith("image/"):
        raise HTTPException(415, "file is not an image")

    content = await file.read()
    await ser.set_back(data=content)


@router.put("/username")
async def put_user_username(
    username: str,
    password: str,
    user: User = Depends(get_user),
):
    ser = UserService(user)

    if not ser.password_matches(password=password):
        raise HTTPException(403, "password does not match")

    await ser.set_username(username=username)


@router.put("/password")
async def put_user_password(
    new_password: str,
    password: str,
    user: User = Depends(get_user),
):
    ser = UserService(user)

    if not ser.password_matches(password=password):
        raise HTTPException(403, "password does not match")

    await ser.set_password(password=new_password)


@router.put("/email")
async def put_user_email(
    email: str,
    password: str,
    user: User = Depends(get_user),
):
    ser = UserService(user)

    if not ser.password_matches(password=password):
        raise HTTPException(403, "password does not match")

    await ser.set_email(email=email)


@router.put("/nickname")
async def put_user_nickname(
    nickname: str,
    user: User = Depends(get_user),
    session: AsyncSession = Depends(get_session),
):
    try:
        user.nickname = nickname
        session.add(user)
        await session.commit()
    except Exception:
        await session.rollback()
        raise HTTPException(500)


@router.put("/status")
async def put_user_status(
    status: str,
    user: User = Depends(get_user),
    session: AsyncSession = Depends(get_session),
):
    try:
        user.status = status
        session.add(user)
        await session.commit()
    except Exception:
        await session.rollback()
        raise HTTPException(500)


@router.put("/about")
async def put_user_about(
    about: str,
    user: User = Depends(get_user),
    session: AsyncSession = Depends(get_session),
):
    try:
        user.about = about
        session.add(user)
        await session.commit()
    except Exception:
        await session.rollback()
        raise HTTPException(500)
