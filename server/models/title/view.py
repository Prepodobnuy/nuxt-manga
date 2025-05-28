from datetime import datetime, timezone

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from ..base import Base


class TitleView(Base):
    __tablename__ = "title_view"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        nullable=False,
        init=False,
    )
    title_id: Mapped[int] = mapped_column(ForeignKey("title.id"))
    user_uuid: Mapped[str] = mapped_column(ForeignKey("user.uuid"))
