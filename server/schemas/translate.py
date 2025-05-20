from pydantic import BaseModel


class TranslateTeamPostScheme(BaseModel):
    description: str | None
    title: str
