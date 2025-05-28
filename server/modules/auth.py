import os
from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, Depends, Request
from jose import JWTError, jwt
from datetime import datetime, timedelta

from sqlalchemy.ext.asyncio import AsyncSession

from models.user.user import User
from modules.permission.roles import Role
from services.user import UserService


SECRET_KEY = "asfghoewgy9w8fy"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
ACCESS_TOKEN_EXPIRE_WEEKS = 4


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
credentials_exception = HTTPException(
    status_code=401,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(weeks=ACCESS_TOKEN_EXPIRE_WEEKS)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_user(token: str = Depends(oauth2_scheme)) -> User:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")  # type:ignore
        if username is None:
            raise credentials_exception
        # type:ignore
        user = await UserService.get_by_username(username=username)
        if user is None:
            raise credentials_exception
        return user
    except JWTError as e:
        print(e)
        raise credentials_exception


async def get_admin(token: str = Depends(oauth2_scheme)) -> User:
    try:
        user = await get_user(token=token)
        if user.role == Role.admin.value:
            return user

    except Exception as e:
        raise e
    raise HTTPException(403)


async def get_moder(token: str = Depends(oauth2_scheme)) -> User:
    try:
        user = await get_user(token=token)
        if user.role == Role.moderator.value or user.role == Role.admin.value:
            return user

    except Exception as e:
        raise e
    raise HTTPException(403)


async def get_not_muted(token: str = Depends(oauth2_scheme)) -> User:
    try:
        user = await get_user(token=token)
        if user.role != Role.muted.value:
            return user

    except Exception as e:
        raise e
    raise HTTPException(403)
