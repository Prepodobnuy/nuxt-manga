from datetime import datetime, timezone

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from ..base import Base


class NotificationGlobal(Base):
    __tablename__ = "notification_global"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        nullable=False,
        init=False,
    )
    description: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(default=datetime.now(timezone.utc))


class NotificationGlobalView(Base):
    __tablename__ = "notification_global_view"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        nullable=False,
        init=False,
    )
    user_uuid: Mapped[str] = mapped_column(ForeignKey("user.uuid"))
    notification_global_id: Mapped[int] = mapped_column(
        ForeignKey("notification_global.id")
    )
