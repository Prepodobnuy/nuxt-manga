from pydantic import BaseModel, Field, fields


class CommentPostScheme(BaseModel):
    page_id: int | None
    title_id: int | None
    comment_id: int | None

    caption: str | None
    deleted: bool = Field(default=False)
    pinned: bool = Field(default=False)

    timestamp: int | None

    reply_count: int | None = Field(0)


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