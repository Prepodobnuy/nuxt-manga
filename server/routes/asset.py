import io
from fastapi import APIRouter, HTTPException, Response
from fastapi.responses import StreamingResponse

from schemas.title import TitleCoverScheme
from services.title.asset import TitleAssetService
from services.title.title import TitleService
from services.user.asset import UserAssetService
from services.user.user import UserService
from services.person.asset import PersonAssetService
from services.person.person import PersonService


router = APIRouter()


@router.get("/title/{title_id}/covers")
async def get_covers(title_id: int) -> list[TitleCoverScheme]:
    title = await TitleService.get_by_id(id=title_id)

    if title is None:
        raise HTTPException(404)

    ser = TitleAssetService(title=title)
    return await ser.list_covers()


@router.get("/title/{title_id}/cover")
async def get_first_title_cover(title_id: int) -> StreamingResponse:
    title = await TitleService.get_by_id(id=title_id)

    if title is None:
        raise HTTPException(404)

    ser = TitleAssetService(title=title)
    data = await ser.get_first_cover()

    if data is None:
        raise HTTPException(404)

    with io.open(data) as content:
        return StreamingResponse(content=content)


@router.get("/title/{title_id}/cover/{cover_id}")
async def get_title_cover(title_id: int, cover_id: int) -> StreamingResponse:
    title = await TitleService.get_by_id(id=title_id)

    if title is None:
        raise HTTPException(404)

    ser = TitleAssetService(title=title)
    data = await ser.get_cover(order=cover_id)

    if data is None:
        raise HTTPException(404)

    with io.open(data) as content:
        return StreamingResponse(content=content)


@router.get("/person/{person_id}/cover")
async def get_person_cover(person_id: int) -> Response:
    person = await PersonService.get_by_id(id=person_id)

    if person is None:
        raise HTTPException(404)

    ser = PersonAssetService(person=person)
    data = await ser.get_cover()

    if data is None:
        raise HTTPException(404)

    return Response(content=data, media_type="image/png")


@router.get("/user/{user_uuid}/pfp")
async def get_user_pfp(user_uuid: str) -> StreamingResponse:
    user = await UserService.get_by_uuid(uuid=user_uuid)
    if user is None:
        raise HTTPException(404)

    ser = UserAssetService(user=user)
    data = await ser.get_pfp()
    if data is None:
        raise HTTPException(404)

    with io.open(data) as content:
        return StreamingResponse(content=content)


@router.get("/user/{user_uuid}/back")
async def get_user_back(user_uuid: str) -> StreamingResponse:
    user = await UserService.get_by_uuid(uuid=user_uuid)
    if user is None:
        raise HTTPException(404)

    ser = UserAssetService(user=user)
    data = await ser.get_back()
    if data is None:
        raise HTTPException(404)

    with io.open(data) as content:
        return StreamingResponse(content=content)
