from uuid import uuid4
from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from modules.permission.roles import Role

from ..base import Base


class User(Base):
    __tablename__ = "user"

    uuid: Mapped[str] = mapped_column(
        primary_key=True,
        nullable=False,
        default=str(uuid4()),
        init=False,
    )
    role: Mapped[str] = mapped_column(
        default=Role.default.value,
        init=False,
    )
    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(unique=True)
    nickname: Mapped[str]
    status: Mapped[str | None] = mapped_column(default=None)
    about: Mapped[str | None] = mapped_column(default=None)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now(), init=False)
