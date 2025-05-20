from datetime import datetime, timezone

from sqlalchemy import ForeignKey
from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column

from typealias.notification import (
    CommentNotificationTypeEnum,
    NotificationTypeEnum,
    PageNotificationTypeEnum,
    ReportNotificationTypeEnum,
    TitleNotificationTypeEnum,
    UserNotificationTypeEnum,
)


from ..base import Base


class Notification(Base):
    __tablename__ = "notification"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        nullable=False,
        init=False,
    )
    target_user_uuid: Mapped[str] = mapped_column(ForeignKey("user.uuid"))
    description: Mapped[str]

    notification_type: Mapped[NotificationTypeEnum] = mapped_column(
        Enum(NotificationTypeEnum)
    )
    user_notification_type: Mapped[UserNotificationTypeEnum | None] = mapped_column(
        Enum(UserNotificationTypeEnum)
    )
    comment_notification_type: Mapped[CommentNotificationTypeEnum | None] = (
        mapped_column(Enum(CommentNotificationTypeEnum))
    )
    title_notification_type: Mapped[TitleNotificationTypeEnum | None] = mapped_column(
        Enum(TitleNotificationTypeEnum),
    )
    page_notification_type: Mapped[PageNotificationTypeEnum | None] = mapped_column(
        Enum(PageNotificationTypeEnum),
    )
    report_notification_type: Mapped[ReportNotificationTypeEnum | None] = mapped_column(
        Enum(ReportNotificationTypeEnum),
    )

    user_uuid: Mapped[str | None] = mapped_column(
        ForeignKey("user.uuid"),
    )
    comment_id: Mapped[int | None] = mapped_column(
        ForeignKey("comment.id"),
    )
    title_id: Mapped[int | None] = mapped_column(
        ForeignKey("title.id"),
    )
    page_id: Mapped[int | None] = mapped_column(
        ForeignKey("page.id"),
    )
    report_id: Mapped[int | None] = mapped_column(
        ForeignKey("report.id"),
    )

    created_at: Mapped[datetime] = mapped_column(default=datetime.now(timezone.utc))
    is_read: Mapped[bool] = mapped_column(default=False)
