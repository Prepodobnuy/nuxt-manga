from datetime import datetime

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column

from ..base import Base


class TranslateTeam(Base):
    __tablename__ = "translate_team"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        init=False,
    )

    owner_uuid: Mapped[str] = mapped_column(ForeignKey("user.uuid"))
    title: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str | None] = mapped_column(default=None)
    fhd: Mapped[str | None] = mapped_column(default=None)
    hd: Mapped[str | None] = mapped_column(default=None)
    sd: Mapped[str | None] = mapped_column(default=None)

    approved: Mapped[bool] = mapped_column(default=False, init=False)
    approved_at: Mapped[datetime | None] = mapped_column(default=None, init=False)
    approved_user_uuid: Mapped[str | None] = mapped_column(
        ForeignKey("user.uuid"), default=None, init=False
    )

    created_at: Mapped[datetime] = mapped_column(server_default=func.now(), init=False)
