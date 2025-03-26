from io import BytesIO

from etc.static import DEFAULT_COVER
from etc.role import role_is_moder, role_is_muted
from .needed import APIRouter, FileResponse, HTTPException, UploadFile, Depends, File
from .needed import get_current_user, get_current_user_unsafe, session
from schemas.person import PersonMetaGetScheme
from schemas.person import PersonMetaPostScheme
from database.tables import PersonMeta, Person, User

router = APIRouter()


@router.get('/{person_id}')
async def get_person(person_id: int, user: User = Depends(get_current_user_unsafe)):
    person: Person = session.query(Person).filter(
        Person.id == person_id).first()

    if person is None:
        raise HTTPException(404)

    if not person.public:
        if user is None:
            raise HTTPException(403)

        if not role_is_moder(user.role):
            raise HTTPException(403)

    return person.get()


@ router.post('')
async def post_person(scheme: PersonMetaPostScheme, user: User = Depends(get_current_user)) -> int:
    if role_is_muted(user.role):
        raise HTTPException(403)

    person = PersonMeta.new(session=session, scheme=scheme, uuid=user.uuid)

    try:
        session.add(person)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()
        raise HTTPException(500)
