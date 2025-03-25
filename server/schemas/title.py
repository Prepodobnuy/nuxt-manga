from pydantic import BaseModel, Field, fields


class TitleMetaPostScheme(BaseModel):
    title_id: int | None
    user_uuid: str

    ru_name: str
    en_name: str
    or_name: str
    an_name: str

    tr_status: str = Field(title='Translate status', examples=['translating', 'translated', 'graveyard'])
    rl_status: str = Field(title='Release status', examples=['ongoing', 'released', 'paused', 'graveyard'])
    title_type: str = Field(title='Type of title', examples=['manga', 'manhua'])

    age_rating: str = Field(title='Age rating', examples=['0+', '12+', '16+', '18+'])
    release_year: int

    tags: str
    genres: str

    author_id: int | None
    artist_id: int | None
    publisher_id: int | None


class TitleMetaGetScheme(BaseModel):
    id: int
    title_id: int
    user_uuid: str

    ru_name: str
    en_name: str
    or_name: str
    an_name: str

    tr_status: str = Field(title='Translate status', examples=['translating', 'translated', 'graveyard'])
    rl_status: str = Field(title='Release status', examples=['ongoing', 'released', 'paused', 'graveyard'])
    title_type: str = Field(title='Type of title', examples=['manga', 'manhua'])

    age_rating: str = Field(title='Age rating', examples=['0+', '12+', '16+', '18+'])
    release_year: int

    tags: str
    genres: str

    timestamp: int

    author_id: int | None
    artist_id: int | None
    publisher_id: int | None

    public: bool = Field(default=False)

    rates_1: int
    rates_2: int
    rates_3: int
    rates_4: int
    rates_5: int
    rates_6: int
    rates_7: int
    rates_8: int
    rates_9: int
    rates_10: int

    rated_value: int | None