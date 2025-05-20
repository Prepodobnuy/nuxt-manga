from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Tag(Base):
    __tablename__ = "tag"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        nullable=False,
        init=False,
    )
    ru: Mapped[str]
    en: Mapped[str]


class Genre(Base):
    __tablename__ = "genre"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        nullable=False,
        init=False,
    )
    ru: Mapped[str]
    en: Mapped[str]
