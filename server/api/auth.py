from fastapi.security import OAuth2PasswordRequestForm

from .needed import *
from auth.auth import create_access_token
from database.tables import User
from schemas.auth import Credentials
from config import hash_string
from etc.constant_data import USERNAME_MIN_LENGTH, USERNAME_MAX_LENGTH
from etc.constant_data import PASSWORD_MIN_LENGTH, PASSWORD_MAX_LENGTH


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
    
    if len(credits.username) > USERNAME_MAX_LENGTH:
        raise HTTPException(400, 'username too long')
    if len(credits.username) < USERNAME_MIN_LENGTH:
        raise HTTPException(400, 'username too short')

    if User.get_user_by_email(session, credits.email) is not None:
        raise HTTPException(400, 'email is taken')
    
    if len(credits.password) > PASSWORD_MAX_LENGTH:
        raise HTTPException(400, 'password too long')
    if len(credits.password) < PASSWORD_MIN_LENGTH:
        raise HTTPException(400, 'password too short')
        
    user = User(credentials=credits)

    try:
        session.add(user)
        session.commit()
    except Exception:
        session.rollback()
        raise HTTPException(500)

    return {'message': 'User registered successfully', 'username': credits.username}
