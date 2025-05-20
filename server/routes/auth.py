from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from modules.auth import create_access_token
from schemas.credentials import Credentials
from services.user import UserService

router = APIRouter()


@router.post("/login")
async def user_login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await UserService.get_by_username(form_data.username)

    if user is None:
        raise HTTPException(status_code=400, detail="incorrect username")
    if not UserService(user=user).password_matches(form_data.password):
        raise HTTPException(status_code=400, detail="incorrect password")

    access_token = create_access_token(data={"sub": user.username})

    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/signup")
async def user_register(credits: Credentials):
    try:
        await UserService.create(
            username=credits.username,
            nickname=credits.username,
            password=credits.password,
            email=credits.email,
        )
    except HTTPException as e:
        raise e
    except Exception as e:
        print(e)
        raise HTTPException(500)

    return {"message": "User registered successfully", "username": credits.username}
