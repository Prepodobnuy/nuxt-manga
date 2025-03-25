from .needed import Base
from .needed import Column, ForeignKey, Integer, String, Boolean
from schemas.rate import CommentCarmaPostScheme
from schemas.rate import TitleRatePostScheme


class CommentCarma(Base):
    __tablename__ = 'comment_carma'
    id = Column(Integer, primary_key=True)
    comment_id = Column(Integer, ForeignKey('comment.id'))
    user_uuid = Column(String, ForeignKey('user.uuid'))
    positive = Column(Boolean)

    def __init__(self, scheme: CommentCarmaPostScheme, uuid: str):
        self.comment_id = scheme.comment_id
        self.user_uuid = uuid
        self.positive = scheme.positive


class TitleRate(Base):
    __tablename__ = 'title_rate'
    id = Column(Integer, primary_key=True)
    title_id = Column(Integer, ForeignKey('title.id'))
    user_uuid = Column(String, ForeignKey('user.uuid'))
    rate = Column(Integer)

    def __init__(self, scheme: TitleRatePostScheme, uuid: str):
        self.title_id = scheme.title_id
        self.user_uuid = uuid
        self.rate = scheme.rate