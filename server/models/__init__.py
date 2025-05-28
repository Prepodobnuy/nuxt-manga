import logging
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

from .assets import TitleCover, TranslateTeamPfp, UserBack, UserPfp, PersonCover
from .user import User
from .title import (
    Title,
    TitleMeta,
    TitleList,
    TitleView,
    TitleRate,
    TitleReadPosition,
    TitleUpdateSubscription,
)
from .person import Person, PersonMeta
from .comment import Comment, CommentCarma
from .translate import (
    TranslateTeam,
    TranslateTeamMember,
    TranslateTeamTitleOwnership,
)
from .tags import Tag, Genre
from .page import Page, PageAsset
from .notification import Notification, NotificationGlobal, NotificationGlobalView
from .report import Report
from .base import Base

from config.db import DATABASE_URL

logger = logging.getLogger(__name__)

__all__ = [
    "TitleCover",
    "TranslateTeamPfp",
    "UserBack",
    "UserPfp",
    "PersonCover",
    "User",
    "Title",
    "TitleMeta",
    "TitleList",
    "TitleView",
    "TitleRate",
    "TitleReadPosition",
    "TitleUpdateSubscription",
    "Person",
    "PersonMeta",
    "Comment",
    "CommentCarma",
    "Tag",
    "Genre",
    "TranslateTeam",
    "TranslateTeamMember",
    "TranslateTeamTitleOwnership",
    "Page",
    "PageAsset",
    "Notification",
    "NotificationGlobal",
    "NotificationGlobalView",
    "Report",
]


def create_metadata():
    logger.debug("create_metadata")

    if not database_exists(DATABASE_URL.replace("+asyncpg", "")):
        create_database(DATABASE_URL.replace("+asyncpg", ""))
    sync_engine = create_engine(DATABASE_URL.replace("+asyncpg", ""))
    Base.metadata.create_all(bind=sync_engine)
