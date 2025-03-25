from pydantic import BaseModel


class UserPublicScheme(BaseModel):
    username: str | None
    email: str | None
    uuid: str
    nickname: str
    status: str
    about: str


class ChangePasswordScheme(BaseModel):
    current_password: str
    new_password: str


class ChangeEmailScheme(BaseModel):
    current_password: str
    new_email: str