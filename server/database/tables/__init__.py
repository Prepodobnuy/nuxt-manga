from database import get_engine, get_session

from .needed import Base
from .user import User 
from .notification import Notification, TitlePageSubscription
from .title import Title, TitleMeta
from .person import Person, PersonMeta
from .comment import Comment
from .page import Page

def initialize():
    engine = get_engine()
    Base.metadata.create_all(bind=engine)
    session = get_session
