from datetime import datetime

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column

from ..base import Base


class TranslateTeamMember(Base):
    __tablename__ = "translate_team_member"

    uuid: Mapped[str] = mapped_column(
        ForeignKey("user.uuid"),
        primary_key=True,
        nullable=False,
        unique=True,
    )
    team_id: Mapped[int] = mapped_column(ForeignKey("translate_team.id"))
    accepted: Mapped[bool] = mapped_column(default=False, init=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now(), init=False)
