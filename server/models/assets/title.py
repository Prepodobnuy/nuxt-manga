from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


from ..base import Base


class TitleCover(Base):
    __tablename__ = "title_cover"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        init=False,
    )

    title_id: Mapped[int] = mapped_column(ForeignKey("title.id"))
    order: Mapped[int]
    data: Mapped[bytes]
    approved: Mapped[bool] = mapped_column(default=False, init=False)
    approved_at: Mapped[datetime | None] = mapped_column(default=None)
    approved_user_uuid: Mapped[str | None] = mapped_column(ForeignKey("user.uuid"), default=None)
