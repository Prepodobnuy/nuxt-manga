from fastapi.security import OAuth2PasswordRequestForm

from .needed import APIRouter, HTTPException, Depends
from .needed import session
from auth.auth import create_access_token
from database.tables import User
from schemas.auth import Credentials
from config import hash_string
from etc.static import USERNAME_RANGE
from etc.static import PASSWORD_RANGE

router = APIRouter()

@router.post('/login')
async def user_login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = User.get_by_username(session, form_data.username)

    if user is None:
        raise HTTPException(status_code=400, detail='incorrect username')

    if user.hashed_password != hash_string(form_data.password):
        raise HTTPException(status_code=400, detail='incorrect password')

    access_token = create_access_token(data={'sub': user.username})

    return {'access_token': access_token, 'token_type': 'bearer'}


@router.post('/signup')
async def user_register(credits: Credentials):
    if User.get_by_username(session, credits.username) is not None:
        raise HTTPException(400, 'username is taken')
    
    if len(credits.username) < USERNAME_RANGE[0]:
        raise HTTPException(400, 'username too short')

    if len(credits.username) > USERNAME_RANGE[1]:
        raise HTTPException(400, 'username too long')

    if User.get_user_by_email(session, credits.email) is not None:
        raise HTTPException(400, 'email is taken')
    
    if len(credits.password) < PASSWORD_RANGE[0]:
        raise HTTPException(400, 'password too short')

    if len(credits.password) > PASSWORD_RANGE[1]:
        raise HTTPException(400, 'password too long')
        
    user = User(credentials=credits)

    try:
        session.add(user)
        session.commit()
    except Exception:
        session.rollback()
        raise HTTPException(500)

    return {'message': 'User registered successfully', 'username': credits.username}