from pydantic import BaseModel


class PersonMetaPostScheme(BaseModel):
    person_id: int | None
    type: str
    ru_name: str | None
    en_name: str | None
    or_name: str | None
    about: str | None


class PersonMetaGetScheme(BaseModel):
    id: int
    person_id: int

    posted_user_uuid: str

    type: str
    ru_name: str
    en_name: str
    or_name: str

    about: str

    timestamp: int

    public: bool
