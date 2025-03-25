from .needed import *


class CommentCarma(Base):
    __tablename__ = 'comment_carma'
    id = Column(Integer, primary_key=True)
    comment_id = Column(Integer, ForeignKey('comment.id'))
    user_uuid = Column(String, ForeignKey('user.uuid'))
    positive = Column(Boolean)

    