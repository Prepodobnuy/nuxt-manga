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
    user_uuid: Mapped[str] = mapped_column(ForeignKey("user.uuid"))
    date: Mapped[datetime] = mapped_column(default=datetime.now(timezone.utc))
