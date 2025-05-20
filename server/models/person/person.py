from datetime import datetime, timezone

from sqlalchemy import ForeignKey, func, text
from sqlalchemy.orm import Mapped, mapped_column

from ..base import Base


class Person(Base):
    __tablename__ = "person"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        nullable=False,
        init=False,
    )
    user_published_uuid: Mapped[str] = mapped_column(ForeignKey("user.uuid"))
    created_at: Mapped[datetime] = mapped_column(
        server_default=text("NOW()"), init=False)
