from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from ..base import Base


class TitleMeta(Base):
    __tablename__ = "title_meta"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        nullable=False,
        init=False,
    )
    title_id: Mapped[int] = mapped_column(ForeignKey("title.id"))
    created_user_uuid: Mapped[str] = mapped_column(ForeignKey("user.uuid"))
    title_ru: Mapped[str]
    title_en: Mapped[str]
    title_jp: Mapped[str]
    release_year: Mapped[int | None]
    title_an: Mapped[str | None] = mapped_column(default=None)
    description: Mapped[str | None] = mapped_column(default=None)
    author_id: Mapped[int | None] = mapped_column(ForeignKey("person.id"), default=None)
    artist_id: Mapped[int | None] = mapped_column(ForeignKey("person.id"), default=None)
    publisher_id: Mapped[int | None] = mapped_column(ForeignKey("person.id"), default=None)
    tags: Mapped[str | None] = mapped_column(default=None)
    genres: Mapped[str | None] = mapped_column(default=None)

    approved: Mapped[bool] = mapped_column(default=False, init=False)
    approved_at: Mapped[datetime | None] = mapped_column(default=None, init=False)
    approved_user_uuid: Mapped[str | None] = mapped_column(
        ForeignKey("user.uuid"), default=None, init=False
    )
