from pydantic import BaseModel


class Credentials(BaseModel):
    username: str
    password: str
    email: str
