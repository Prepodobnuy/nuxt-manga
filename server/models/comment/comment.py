from datetime import datetime, timezone

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from ..base import Base


class Comment(Base):
    __tablename__ = "comment"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        nullable=False,
        init=False,
    )
    user_uuid: Mapped[str] = mapped_column(ForeignKey("user.uuid"))
    caption: Mapped[str]
    reply_to: Mapped[int | None] = mapped_column(ForeignKey("comment.id"), default=None)
    page_id: Mapped[int | None] = mapped_column(ForeignKey("page.id"), default=None)
    title_id: Mapped[int | None] = mapped_column(ForeignKey("title.id"), default=None)
    deleted: Mapped[bool] = mapped_column(default=False, init=False)
    pinned: Mapped[bool] = mapped_column(default=False, init=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now(timezone.utc))
