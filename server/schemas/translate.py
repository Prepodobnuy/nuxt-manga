from pydantic import BaseModel


class TranslateTeamPostScheme(BaseModel):
    description: str | None
    title: str


class TranslateTeamMemberScheme(BaseModel):
    uuid: str
    team_id: int
    accepted: bool


class TranslateTeamScheme(BaseModel):
    id: int
    owner_uuid: str
    title: str
    description: str | None
    approved: bool
    accepted_members: list[TranslateTeamMemberScheme]
    unaccepted_members: list[TranslateTeamMemberScheme]
