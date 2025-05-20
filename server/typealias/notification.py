from enum import Enum
from typing import Literal, TypeAlias


NotificationType: TypeAlias = Literal[
    "user_notification",
    "comment_notification",
    "title_notification",
    "page_notification",
    "report_notification",
    "global_notification",
]

UserNotificationType: TypeAlias = Literal[
    "role_changed",
    "data_changed",
]

CommentNotificationType: TypeAlias = Literal[
    "highrated",
    "deleted",
    "replyed",
]

TitleNotificationType: TypeAlias = Literal[
    "meta_accepted",
    "cover_accepted",
]

PageNotificationType: TypeAlias = Literal["new_page_added"]

ReportNotificationType: TypeAlias = Literal[
    "report_resolved",
    "report_rejected",
]

GlobalNotificationType: TypeAlias = Literal["global"]


class NotificationTypeEnum(str, Enum):
    USER = "user_notification"
    COMMENT = "comment_notification"
    TITLE = "title_notification"
    PAGE = "page_notification"
    REPORT = "report_notification"
    GLOBAL = "global_notification"


class UserNotificationTypeEnum(str, Enum):
    ROLE_CHANGED = "role_changed"
    DATA_CHANGED = "data_changed"


class CommentNotificationTypeEnum(str, Enum):
    HIGHRATED = "highrated"
    DELETED = "deleted"
    REPLYED = "replyed"


class TitleNotificationTypeEnum(str, Enum):
    META_ACCEPTED = "meta_accepted"
    COVER_ACCEPTED = "cover_accepted"


class PageNotificationTypeEnum(str, Enum):
    NEW_PAGE_ADDED = "new_page_added"


class ReportNotificationTypeEnum(str, Enum):
    RESOLVED = "report_resolved"
    REJECTED = "report_rejected"


class GlobalNotificationTypeEnum(str, Enum):
    GLOBAL = "global"
