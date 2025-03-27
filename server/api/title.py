from io import BytesIO

from etc.static import DEFAULT_COVER
from etc.role import role_is_moder, role_is_muted
from .needed import APIRouter, FileResponse, HTTPException, UploadFile, Depends, File, RedirectResponse
from .needed import get_current_user, get_current_user_unsafe, session
from schemas.title import TitleMetaPostScheme
from schemas.title import TitleMetaGetScheme
from database.tables import TitleMeta, Title, User

router = APIRouter()


@router.get('/{id}')
async def get_title_meta(
    id: int, user: User = Depends(get_current_user_unsafe)
) -> TitleMetaGetScheme:
    title_meta = session.query(TitleMeta).filter(TitleMeta.id == id).first()

    if title_meta is None:
        raise HTTPException(404)

    if user is None:
        if title_meta.public:
            return title_meta.get(session=session, uuid=None)

        raise HTTPException(403)

    if title_meta.public:
        return title_meta.get(session=session, uuid=user.uuid)

    if role_is_moder(user.role):
        return title_meta.get(session=session, uuid=user.uuid)

    raise HTTPException(403)


@router.post('')
async def post_title(
    scheme: TitleMetaPostScheme, user: User = Depends(get_current_user)
) -> int:
    if role_is_muted(user.role):
        raise HTTPException(403)

    meta = TitleMeta.new(session=session, scheme=scheme, uuid=user.uuid)

    try:
        session.add(meta)
        session.commit()
        return meta.id
    except Exception as e:
        print(e)
        session.rollback()
        raise HTTPException(500)


@router.post('/{title_meta_id}/cover')
async def post_title_cover(
    title_meta_id: int,
    file: UploadFile = File(...),
    user: User = Depends(get_current_user),
):
    if role_is_muted(user.role):
        raise HTTPException(403)

    title_meta = session.query(TitleMeta).filter(
        TitleMeta.id == title_meta_id).first()

    if title_meta is None:
        raise HTTPException(404)

    if title_meta.user_uuid != user.uuid and not role_is_moder(user.role):
        raise HTTPException(403)

    if not file.content_type.startswith('image/'):
        raise HTTPException(400, 'file is not an image')

    contents = await file.read()
    title_meta.set_cover(BytesIO(contents))


@router.get('/{title_id}/cover')
async def get_title_cover(title_id: int) -> FileResponse:
    try:
        title: Title = session.query(Title).filter(
            Title.id == title_id).first()

        meta = session.query(TitleMeta).filter(
            TitleMeta.title_id == title.id).filter(TitleMeta.public is True).first()

        return FileResponse(meta.uhd_cover)

    except Exception as e:
        print(e)

    return FileResponse(DEFAULT_COVER)


@router.put('/{title_id}')
async def update_title_meta(
    title_id: int, scheme: TitleMetaPostScheme, user: User = Depends(get_current_user)
) -> int:
    if role_is_muted(user.role):
        raise HTTPException(403)

    title = session.query(Title).filter(Title.id == title_id).first()

    if title is None:
        raise HTTPException(404)

    meta = TitleMeta.new(session=session, scheme=scheme, uuid=user.uuid)

    if meta is None:
        raise HTTPException(423, 'too many pending data')

    try:
        session.add(meta)
        session.commit()
        return meta.id
    except Exception as e:
        print(e)
        session.rollback()
        raise HTTPException(500)


@router.post('/approve/{title_meta_id}')
async def approve_title_meta(
    title_meta_id: int, user: User = Depends(get_current_user)
):
    if not role_is_moder(user.role):
        raise HTTPException(403)

    meta = session.query(TitleMeta).filter(
        TitleMeta.id == title_meta_id).first()

    if meta is None:
        raise HTTPException(404)

    if meta.public is True:
        raise HTTPException(400)

    current_approved_meta = (
        session.query(TitleMeta).filter(TitleMeta.public is True).first()
    )

    if current_approved_meta is not None:
        try:
            session.delete(current_approved_meta)
            session.commit()
        except Exception as e:
            print(e)
            session.rollback()
            raise HTTPException(500)

    meta.public = True
    try:
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()
        raise HTTPException(500)


@router.post('/disapprove/{title_id}')
async def disapprove_title_meta(title_id: int, user: User = Depends(get_current_user)):
    if not role_is_moder(user.role):
        raise HTTPException(403)

    meta = (
        session.query(TitleMeta)
        .filter(TitleMeta.title_id == title_id)
        .filter(TitleMeta.public is True)
        .first()
    )

    if meta is None:
        raise HTTPException(404)

    try:
        session.delete(meta)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()
        raise HTTPException(500)


@router.delete('/{title_id}')
async def delete_title(title_id: int, user: User = Depends(get_current_user)):
    if not role_is_moder(user.role):
        raise HTTPException(403)

    title = session.query(Title).filter(Title.id == title_id).first()

    if title is None:
        raise HTTPException(404)

    meta = session.query(TitleMeta).filter(
        TitleMeta.title_id == title.id).all()

    try:
        for m in meta:
            session.delete(m)
        session.delete(title)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()
        raise HTTPException(500)


@router.delete('/{title_meta_id}')
async def delete_title_meta(title_meta_id: int, user: User = Depends(get_current_user)):
    if not role_is_moder(user.role):
        raise HTTPException(403)

    meta = session.query(TitleMeta).filter(
        TitleMeta.id == title_meta_id).first()

    if meta is None:
        raise HTTPException(404)

    try:
        session.delete(meta)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()
        raise HTTPException(500)
