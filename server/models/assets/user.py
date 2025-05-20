from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


from ..base import Base


class UserPfp(Base):
    __tablename__ = "user_pfp"

    uuid: Mapped[str] = mapped_column(ForeignKey("user.uuid"), primary_key=True)
    data: Mapped[bytes]


class UserBack(Base):
    __tablename__ = "user_back"

    uuid: Mapped[str] = mapped_column(ForeignKey("user.uuid"), primary_key=True)
    data: Mapped[bytes]
