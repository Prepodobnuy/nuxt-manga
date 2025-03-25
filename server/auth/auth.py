from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, Depends
from jose import JWTError, jwt
from datetime import datetime, timedelta

from database.tables import User
from database.session import get_session
from config import SECRET_KEY


ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
ACCESS_TOKEN_EXPIRE_WEEKS = 4


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(weeks=ACCESS_TOKEN_EXPIRE_WEEKS)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")

        if username is None: 
            raise credentials_exception

        user = User.get_by_username(get_session(), username)

        if user is None: 
            raise credentials_exception

        return user
    except JWTError:
        raise credentials_exception
    

def get_current_user_unsafe(token: str = Depends(oauth2_scheme)) -> User | None:
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")

        if username is None: 
            raise credentials_exception

        user = User.get_by_username(get_session(), username)

        if user is None: 
            raise credentials_exception

        return user
    except JWTError:
        return None