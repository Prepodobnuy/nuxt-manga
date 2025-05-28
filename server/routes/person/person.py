import json
from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from config.assets import PERSON_COVER_RESOLUTION
from db.session_fabric import get_session
from models.person.personmeta import PersonMeta
from models.user.user import User
from modules.auth import get_moder, get_not_muted, get_user
from modules.permission.roles import Role
from schemas.person import PersonMetaPostScheme, PersonScheme
from services.asset import AssetService
from services.person.asset import PersonAssetService
from services.person.person import PersonService
from services.person.person_meta import PersonMetaService


router = APIRouter()


@router.get("/search/{prompt}")
async def quick_search(prompt: str) -> list[PersonScheme]:
    results = await PersonService.quick_search(prompt=prompt)
    print(results)
    return [await PersonService(person=p).to_scheme(include_unaproved_meta=False) for p in results]


@router.get("/unaproved")
async def get_unproved_persons(user: User = Depends(get_moder)) -> list[PersonScheme]:
    results = await PersonService.get_unaproved()
    return [await PersonService(person=p).to_scheme(include_unaproved_meta=False) for p in results]


@router.get("/{id}")
async def get_person(id: int, user: User = Depends(get_user)) -> PersonScheme:
    person = await PersonService.get_by_id(id=id)

    if person is None:
        raise HTTPException(404)

    if user.role == Role.moderator.value or user.role == Role.admin.value:
        return await PersonService(person=person).to_scheme(include_unaproved_meta=True)
    return await PersonService(person=person).to_scheme(include_unaproved_meta=False)


@router.post("/")
async def post_person(
    file: UploadFile = File(...),
    scheme: str = Form(...),
    user: User = Depends(get_moder),
    session: AsyncSession = Depends(get_session),
):
    if file.content_type is None:
        raise HTTPException(415, "no file supplied")
    if not file.content_type.startswith("image/"):
        raise HTTPException(415, "file is not an image")
    try:
        parsed = PersonMetaPostScheme(**json.loads(scheme))
    except Exception:
        raise HTTPException(400)

    async with session:
        try:
            person = PersonService.create(user=user)
            session.add(person)
            await session.flush()

            meta = PersonMeta(
                person_id=person.id,
                created_user_uuid=user.uuid,
                name_ru=parsed.name_ru,
                name_en=parsed.name_en,
                name_jp=parsed.name_jp,
                name_an=parsed.name_an,
                description=parsed.description,
            )
            meta.approved = True
            session.add(meta)

            content = await file.read()
            cover_service = PersonAssetService(person=person)
            await cover_service.set_cover(data=content, session=session)

            await session.commit()
        except Exception as e:
            print("\n\n\n", e, "\n\n\n")
            await session.rollback()
            raise HTTPException(500)


@router.post("/{person_id}")
async def put_person_cover(
    person_id: int,
    file: UploadFile = File(...),
    user: User = Depends(get_moder),
):
    if file.content_type is None:
        raise HTTPException(415, "no file supplied")
    if not file.content_type.startswith("image/"):
        raise HTTPException(415, "file is not an image")

    person = await PersonService.get_by_id(id=person_id)

    if person is None:
        raise HTTPException(404)

    content = await file.read()

    cover = PersonAssetService(person=person)
    await cover.set_cover(data=content)


@router.delete("/{id}")
async def delete_person(id: int, user: User = Depends(get_moder)):
    person = await PersonService.get_by_id(id=id)

    if person is None:
        raise HTTPException(404)

    await PersonService(person=person).delete()
