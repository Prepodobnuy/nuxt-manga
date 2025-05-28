from pydantic import BaseModel


class PagePostScheme(BaseModel):
    volume: int
    chapter: int
    order: int


class PageScheme(BaseModel):
    id: int
    volume: int
    chapter: int
    order: int
