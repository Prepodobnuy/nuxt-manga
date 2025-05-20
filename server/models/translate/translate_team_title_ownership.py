from datetime import datetime

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column

from ..base import Base


class TranslateTeamTitleOwnership(Base):
    __tablename__ = "translate_team_title_ownership"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        init=False,
    )
    title_id: Mapped[int] = mapped_column(ForeignKey("title.id"))
    team_id: Mapped[int] = mapped_column(ForeignKey("translate_team.id"))
    created_at: Mapped[datetime] = mapped_column(server_default=func.now(), init=False)
