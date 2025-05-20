from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from ..base import Base


class TitleList(Base):
    __tablename__ = "title_list"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        nullable=False,
        init=False,
    )
    user_uuid: Mapped[str] = mapped_column(ForeignKey("user.uuid"))
    title_id: Mapped[int] = mapped_column(ForeignKey("title.id"))
    name: Mapped[str]
