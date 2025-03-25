from .needed import *
from schemas.rate import CommentCarmaPostScheme


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