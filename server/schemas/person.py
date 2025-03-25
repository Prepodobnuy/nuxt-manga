from pydantic import BaseModel


class PersonMetaScheme(BaseModel):
    id: int | None
    person_id: int | None

    posted_user_uuid: str | None

    type: str | None
    ru_name: str | None
    en_name: str | None
    or_name: str | None

    about: str | None

    public: bool

