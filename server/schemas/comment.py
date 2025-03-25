from pydantic import BaseModel, Field, fields
from etc.constant_data import COMMENT_LENGTH_RANGE


class CommentPostScheme(BaseModel):
    page_id: int | None
    title_id: int | None
    comment_id: int | None

    caption: str = Field(..., ge=COMMENT_LENGTH_RANGE[0], le=COMMENT_LENGTH_RANGE[1])


class CommentGetScheme(BaseModel):
    id: int
    page_id: int | None
    title_id: int | None
    comment_id: int | None
    user_uuid: str

    caption: str
    deleted: bool
    pinned: bool

    timestamp: int

    replies: int = Field(default=0)

    carma: int