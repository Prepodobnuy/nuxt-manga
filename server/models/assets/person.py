from datetime import datetime, timezone
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


from ..base import Base


class PersonCover(Base):
    __tablename__ = "person_cover"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        init=False,
    )

    person_id: Mapped[int] = mapped_column(ForeignKey("person.id"))
    data: Mapped[bytes]
