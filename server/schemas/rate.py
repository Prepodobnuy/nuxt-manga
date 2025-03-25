from pydantic import BaseModel, Field, fields


class CommentCarmaPostScheme(BaseModel):
    comment_id: int
    positive: bool