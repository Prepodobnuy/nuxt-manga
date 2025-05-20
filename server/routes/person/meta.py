import json
from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile

from config.assets import PERSON_COVER_RESOLUTION
from models.user.user import User
from modules.auth import get_moder, get_not_muted, get_user
from modules.permission.roles import Role
from schemas.person import PersonMetaPostScheme, PersonMetaScheme, PersonScheme
from services.asset import AssetService
from services.person.person import PersonService
from services.person.person_meta import PersonMetaService


router = APIRouter()


@router.get("/{id}")
async def get_person_meta(id: int, user: User = Depends(get_user)) -> PersonMetaScheme:
    meta = await PersonMetaService.get_by_id(id=id)

    if meta is None:
        raise HTTPException(404)

    if user.role == Role.moderator.value or user.role == Role.admin.value:
        return PersonMetaService(meta=meta).to_scheme()

    if meta.approved:
        return PersonMetaService(meta=meta).to_scheme()

    raise HTTPException(404)


@router.post("/{id}/approve")
async def post_approve_person_meta(id: int, user: User = Depends(get_moder)):
    meta = await PersonMetaService.get_by_id(id=id)

    if meta is None:
        raise HTTPException(404)

    await PersonMetaService(meta=meta).approve(user=user)


@router.put("/{id}")
async def put_person_meta(
    id: int,
    scheme: PersonMetaPostScheme,
    user: User = Depends(get_moder),
):
    person = await PersonService.get_by_id(id=id)

    if person is None:
        raise HTTPException(404)

    await PersonMetaService.create_from_scheme(
        user=user,
        person=person,
        scheme=scheme,
    )


@router.delete("/{id}")
async def delete_person_meta(id: int, user: User = Depends(get_moder)):
    meta = await PersonMetaService.get_by_id(id=id)

    if meta is None:
        raise HTTPException(404)

    await PersonMetaService(meta=meta).delete()
