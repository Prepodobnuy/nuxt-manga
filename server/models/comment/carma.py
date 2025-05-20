from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from ..base import Base


class CommentCarma(Base):
    __tablename__ = "comment_carma"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        nullable=False,
        init=False,
    )
    comment_id: Mapped[int] = mapped_column(ForeignKey("comment.id"))
    user_rated: Mapped[str] = mapped_column(ForeignKey("user.uuid"))
    positive: Mapped[bool]
