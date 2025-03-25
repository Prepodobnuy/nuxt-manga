from pydantic import BaseModel, Field, fields


class TitleMetaScheme(BaseModel):
    id: int | None
    title_id: int | None

    posted_user_uuid: str | None

    ru_name: str | None
    en_name: str | None
    or_name: str | None
    an_name: str | None

    tr_status: str | None = Field(title='Translate status', examples=['translating', 'translated', 'graveyard'])
    rl_status: str | None = Field(title='Release status', examples=['ongoing', 'released', 'paused', 'graveyard'])
    title_type: str | None = Field(title='Type of title', examples=['manga', 'manhua'])

    age_rating: str | None = Field(title='Age rating', examples=['0+', '12+', '16+', '18+'])
    release_year: int | None

    tags: str | None
    genres: str | None

    timestamp: int | None

    author_id: int | None
    artist_id: int | None
    publisher_id: int | None

    public: bool = Field(default=False)