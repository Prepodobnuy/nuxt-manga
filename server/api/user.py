from io import BytesIO

from etc.static import DEFAULT_PFP
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


@router.get('/{uuid}/pfp/uhd')
async def get_user_pfp(uuid: str) -> FileResponse:
    user: User = User.get_by_uuid(session, uuid)

    if user is None: 
        raise HTTPException(404)

    if user.uhd_path is None: 
        return FileResponse(DEFAULT_PFP)

    return FileResponse(user.uhd_path)


@router.get('/{uuid}/pfp/hd')
async def get_user_pfp(uuid: str) -> FileResponse:
    user: User = User.get_by_uuid(session, uuid)

    if user is None: 
        raise HTTPException(404)

    if user.hd_path is None: 
        return FileResponse(DEFAULT_PFP)

    return FileResponse(user.hd_path)


@router.get('/{uuid}/pfp/sd')
async def get_user_pfp(uuid: str) -> FileResponse:
    user: User = User.get_by_uuid(session, uuid)

    if user is None: 
        raise HTTPException(404)

    if user.sd_path is None: 
        return FileResponse(DEFAULT_PFP)

    return FileResponse(user.sd_path)


@router.post('/pfp')
async def post_pfp(file: UploadFile = File(...), user: User = Depends(get_current_user)):
    if user is None: 
        raise HTTPException(403)
        
    if not file.content_type.startswith("image/"):
        raise HTTPException(400, 'file is not an image')
    
    contents = await file.read()
    user.set_pfp(BytesIO(contents))