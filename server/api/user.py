from io import BytesIO
import os

from etc.static import DEFAULT_PFP
from etc.role import role_is_admin
from .needed import APIRouter, FileResponse, HTTPException, UploadFile, Depends, File
from .needed import get_current_user, session
from schemas.user import UserPublicScheme
from database.tables import User

router = APIRouter()


@router.get('/{uuid}')
async def get_user_public_data(uuid: str) -> UserPublicScheme | None:
    user: User = User.get_by_uuid(session, uuid)

    if user is None:
        raise HTTPException(404)

    return user.public_scheme()


@router.get('/{uuid}/pfp')
async def get_user_pfp(uuid: str) -> FileResponse:
    user: User = User.get_by_uuid(session, uuid)

    if user is None:
        raise HTTPException(404)

    if user.uhd_path is None:
        return FileResponse(DEFAULT_PFP)

    return FileResponse(user.uhd_path)


@router.post('/pfp')
async def post_pfp(file: UploadFile = File(...), user: User = Depends(get_current_user)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(400, 'file is not an image')

    contents = await file.read()
    user.set_pfp(BytesIO(contents))


@router.delete('')
async def delete_user(user: User = Depends(get_current_user)):
    try:
        os.remove(user.uhd_path)
        os.remove(user.hd_path)
        os.remove(user.sd_path)
    except Exception as e:
        print(e)

    try:
        session.delete(user)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()
        raise HTTPException(500)


@router.delete('/{uuid}')
async def delete_user(uuid: str, user: User = Depends(get_current_user)):
    if not role_is_admin(user.role):
        raise HTTPException(403)

    vilain = User.get_by_uuid(session, uuid)

    if vilain is None:
        raise HTTPException(404)

    try:
        session.delete(vilain)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()
        raise HTTPException(500)
