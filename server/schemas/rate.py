from pydantic import BaseModel, Field, fields


class CommentCarmaPostScheme(BaseModel):
    comment_id: int
    positive: bool


class TitleRatePostScheme(BaseModel):
    title_id: int
    rate: int = Field(..., ge=1, le=10)