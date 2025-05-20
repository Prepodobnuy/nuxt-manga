from datetime import datetime, timezone

from sqlalchemy import ForeignKey, func, text
from sqlalchemy.orm import Mapped, mapped_column

from ..base import Base


class PersonMeta(Base):
    __tablename__ = "personmeta"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        nullable=False,
        init=False,
    )
    person_id: Mapped[int] = mapped_column(ForeignKey("person.id"))
    created_user_uuid: Mapped[str] = mapped_column(ForeignKey("user.uuid"))

    name_ru: Mapped[str]
    name_en: Mapped[str]
    name_jp: Mapped[str]
    name_an: Mapped[str | None] = mapped_column(default=None)
    description: Mapped[str | None] = mapped_column(default=None)

    approved: Mapped[bool] = mapped_column(default=False, init=False)
    approved_at: Mapped[datetime | None] = mapped_column(
        default=None, init=False)
    approved_user_uuid: Mapped[str | None] = mapped_column(
        ForeignKey("user.uuid"), default=None, init=False
    )

    created_at: Mapped[datetime] = mapped_column(
        server_default=text("NOW()"), init=False)
