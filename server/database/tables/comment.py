from .needed import *
from .rate import CommentCarma
from schemas.comment import CommentPostScheme
from schemas.comment import CommentGetScheme


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    page_id = Column(Integer, ForeignKey('page.id'), nullable=True)
    title_id = Column(Integer, ForeignKey('title.id'), nullable=True)
    comment_id = Column(Integer, ForeignKey('comment.id'), nullable=True)
    user_uuid = Column(String, ForeignKey('user.uuid'))

    caption = Column(String)
    deleted = Column(Boolean, default=False)
    pinned = Column(Boolean, default=False)

    timestamp = Column(Integer)


    def __init__(self, scheme: CommentPostScheme, uuid: str):
        self.page_id = scheme.page_id
        self.title_id = scheme.title_id
        self.comment_id = scheme.comment_id
        self.user_uuid = uuid

        self.caption = scheme.caption
        self.deleted = False
        self.pinned = False

        self.timestamp = timestamp()


    def get(self, session: Session) -> CommentGetScheme:
        CommentGetScheme(
            id=self.id,
            page_id=self.page_id,
            title_id=self.title_id,
            comment_id=self.comment_id,
            user_uuid=self.user_uuid,
            caption=self.caption,
            deleted=self.deleted,
            pinned=self.pinned,
            timestamp=self.timestamp,
            replies=len(get_replies(session, self.id)),
            carma=count_carma(session, self.id),
        )


def get_replies(session: Session, id: int) -> list[Comment]:
    return session.query(Comment).filter(Comment.comment_id == id).all()

def count_carma(session: Session, id: int) -> int:
    positive = len(session.query(CommentCarma).filter(CommentCarma.comment_id == id).filter(CommentCarma.positive == True).all())
    negative = len(session.query(CommentCarma).filter(CommentCarma.comment_id == id).filter(CommentCarma.positive == False).all())
    return positive - negative