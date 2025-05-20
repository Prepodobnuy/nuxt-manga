from datetime import datetime
from pydantic import BaseModel


class PersonMetaScheme(BaseModel):
    id: int
    person_id: int
    created_user_uuid: str
    name_ru: str
    name_en: str
    name_jp: str
    name_an: str | None
    description: str | None

    approved: bool
    approved_at: datetime | None
    approved_user_uuid: str | None
    created_at: datetime


class PersonScheme(BaseModel):
    id: int
    user_published_uuid: str

    created_at: datetime

    meta: PersonMetaScheme | None
    unapproved_metas: list[PersonMetaScheme]


class PersonMetaPostScheme(BaseModel):
    name_ru: str
    name_en: str
    name_jp: str
    name_an: str | None
    description: str | None
