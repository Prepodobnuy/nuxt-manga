from datetime import datetime
from pydantic import BaseModel


class UserScheme(BaseModel):
    uuid: str
    role: str
    username: str
    email: str
    nickname: str
    status: str | None
    about: str | None
    muted: bool
    moder: bool
    admin: bool
    translator: bool
    owns_translate_team: bool
    created_at: datetime
