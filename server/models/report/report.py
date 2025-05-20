from datetime import datetime, timezone
from sqlalchemy import ForeignKey
from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column

from typealias.report import (
    CommentReportTypeEnum,
    PageReportTypeEnum,
    ReportStatus,
    ReportTypeEnum,
    TitleReportTypeEnum,
    UserReportTypeEnum,
)

from ..base import Base


class Report(Base):
    __tablename__ = "report"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        nullable=False,
        init=False,
    )

    caption: Mapped[str]
    created_user_uuid: Mapped[str] = mapped_column(ForeignKey("user.uuid"))
    created_at: Mapped[datetime] = mapped_column(
        default=datetime.now(timezone.utc), init=False
    )

    report_type: Mapped[ReportTypeEnum] = mapped_column(Enum(ReportTypeEnum))
    user_report_type: Mapped[UserReportTypeEnum | None] = mapped_column(
        Enum(UserReportTypeEnum), default=None
    )
    comment_report_type: Mapped[CommentReportTypeEnum | None] = mapped_column(
        Enum(CommentReportTypeEnum), default=None
    )
    title_report_type: Mapped[TitleReportTypeEnum | None] = mapped_column(
        Enum(TitleReportTypeEnum), default=None
    )
    page_report_type: Mapped[PageReportTypeEnum | None] = mapped_column(
        Enum(PageReportTypeEnum), default=None
    )

    user_uuid: Mapped[str | None] = mapped_column(ForeignKey("user.uuid"), default=None)
    comment_id: Mapped[int | None] = mapped_column(
        ForeignKey("comment.id"), default=None
    )
    title_id: Mapped[int | None] = mapped_column(ForeignKey("title.id"), default=None)
    page_id: Mapped[int | None] = mapped_column(ForeignKey("page.id"), default=None)

    status: Mapped[ReportStatus] = mapped_column(default="pending", init=False)
