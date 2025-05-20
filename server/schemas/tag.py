from pydantic import BaseModel


class TagScheme(BaseModel):
    id: int
    ru: str
    en: str
