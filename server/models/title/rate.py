from typing import Literal

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from ..base import Base


class TitleRate(Base):
    __tablename__ = "title_rate"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        nullable=False,
        init=False,
    )
    title_id: Mapped[int] = mapped_column(ForeignKey("title.id"))
    user_uuid: Mapped[str] = mapped_column(ForeignKey("user.uuid"))
    rating: Mapped[int] = mapped_column(Integer)

    def __post_init__(self):
        if self.rate:
            self.rate = max(min(5, self.rate), 1)
        else:
            self.rate = 1
