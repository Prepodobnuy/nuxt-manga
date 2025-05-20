from datetime import datetime

from pydantic import BaseModel

from typealias.title import ListName


class TitleMetaScheme(BaseModel):
    id: int
    title_id: int

    title_ru: str
    title_en: str
    title_jp: str
    title_an: str | None

    description: str | None

    author_id: int | None
    artist_id: int | None
    publisher_id: int | None

    tags: list[int]
    genres: list[int]

    approved: bool
    approved_at: datetime | None
    approved_user_uuid: str | None

    created_user_uuid: str
    created_at: datetime


class TitlesMetaSchemes(BaseModel):
    title_id: int
    metas: list[TitleMetaScheme]


class TitleMetaPostScheme(BaseModel):
    title_ru: str
    title_en: str
    title_jp: str
    title_an: str | None

    release_year: str

    description: str | None

    author_id: int
    artist_id: int
    publisher_id: int

    tags: list[int]
    genres: list[int]


class TitleCoverScheme(BaseModel):
    id: int
    title_id: int
    order: int


class TitlePublicScheme(BaseModel):
    id: int

    meta: TitleMetaScheme | None
    covers: list[TitleCoverScheme]

    created_user_uuid: str
    created_at: datetime


class TitlePrivatScheme(BaseModel):
    id: int

    meta: list[TitleMetaScheme]
    covers: list[TitleCoverScheme]

    created_user_uuid: str
    created_at: datetime


class TitleRateGetScheme(BaseModel):
    rates_5: int
    rates_4: int
    rates_3: int
    rates_2: int
    rates_1: int


class TitleUserRateScheme(BaseModel):
    rate: int | None


class TitleListScheme(BaseModel):
    reading: int
    planned: int
    graveyard: int
    readed: int
    loved: int
    another: int


class TitleUserListScheme(BaseModel):
    list_name: ListName


class TitleUserReadPositionScheme(BaseModel):
    id: int
    user_uuid: str
    title_id: int
    page_id: int
    created_at: datetime
