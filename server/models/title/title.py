from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from ..base import Base


class Title(Base):
    __tablename__ = "title"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        nullable=False,
        init=False,
    )

    created_user_uuid: Mapped[str] = mapped_column(ForeignKey("user.uuid"))
