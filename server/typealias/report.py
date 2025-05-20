from enum import Enum
from typing import Literal, TypeAlias


ReportType: TypeAlias = Literal[
    "user_report",
    "comment_report",
    "title_report",
    "page_report",
]

ReportStatus: TypeAlias = Literal[
    "pending",
    "resolved",
    "rejected",
]

UserReportType: TypeAlias = Literal[
    "explicit_content",
    "privelledge_abuse",
    "another",
]

CommentReportType: TypeAlias = Literal[
    "spam",
    "offtop",
    "spoiler",
    "another",
]

TitleReportType: TypeAlias = Literal[
    "inappropriate_meta",
    "inappropriate_cover",
    "spam_page",
    "another",
]

PageReportType: TypeAlias = Literal[
    "inappropriate_caption",
    "another",
]


class ReportTypeEnum(Enum):
    USER_REPORT = "user_report"
    COMMENT_REPORT = "comment_report"
    TITLE_REPORT = "title_report"
    PAGE_REPORT = "page_report"


class UserReportTypeEnum(Enum):
    EXPLICIT_CONTENT = "explicit_content"
    PRIVILEGE_ABUSE = "privilege_abuse"
    ANOTHER = "another"


class CommentReportTypeEnum(Enum):
    SPAM = "spam"
    OFFTOP = "offtop"
    SPOILER = "spoiler"
    ANOTHER = "another"


class TitleReportTypeEnum(Enum):
    INAPPROPRIATE_META = "inappropriate_meta"
    INAPPROPRIATE_COVER = "inappropriate_cover"
    SPAM_PAGE = "spam_page"
    ANOTHER = "another"


class PageReportTypeEnum(Enum):
    INAPPROPRIATE_CAPTION = "inappropriate_caption"
    ANOTHER = "another"
