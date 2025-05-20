from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from ..base import Base


class PageAsset(Base):
    __tablename__ = "page_asset"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        nullable=False,
        init=False,
    )
    page_id: Mapped[int] = mapped_column(ForeignKey("page.id"))
    translate_team_id: Mapped[int] = mapped_column(ForeignKey("translate_team.id"))
    asset_path: Mapped[str]
