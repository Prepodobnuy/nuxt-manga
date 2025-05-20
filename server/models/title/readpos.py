from datetime import datetime, timezone

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from ..base import Base


class TitleReadPosition(Base):
    __tablename__ = "title_read_position"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        nullable=False,
        init=False,
    )
    user_uuid: Mapped[str] = mapped_column(ForeignKey("user.uuid"))
    title_id: Mapped[int] = mapped_column(ForeignKey("title.id"))
    page_id: Mapped[int] = mapped_column(ForeignKey("page.id"))
    created_at: Mapped[datetime] = mapped_column(
        default=datetime.now(timezone.utc), init=False
    )
