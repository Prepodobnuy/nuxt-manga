from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


from ..base import Base


class TranslateTeamPfp(Base):
    __tablename__ = "tranlate_team_pfp"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        init=False,
    )

    translate_team_id: Mapped[int] = mapped_column(ForeignKey("translate_team.id"))
    data: Mapped[bytes]
