from pydantic import BaseModel

from schemas.title import TitleMetaScheme


class SearchPostScheme(BaseModel):
    prompt: str | None

    include_tags: list[int]
    exclude_tags: list[int]

    include_genres: list[int]
    exclude_genres: list[int]

    release_year_min: int | None
    release_year_max: int | None

    rate_min: int | None
    rate_max: int | None

    descending_order: bool
    sort_by_views: bool
    sort_by_rating: bool

    index: int


class SearchResultScheme(BaseModel):
    end: bool
    titles: list[TitleMetaScheme]
