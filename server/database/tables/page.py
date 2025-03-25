from .needed import *


class Page(Base):
    __tablename__ = 'page'

    id = Column(Integer, primary_key=True)
    user_uuid = Column(String, ForeignKey('user.uuid'))
    title_id = Column(Integer, ForeignKey('title.id'))

    tome = Column(Integer, nullable=False)
    chapter = Column(Integer, nullable=False)
    page = Column(Integer, nullable=False)
    public = Column(Boolean, nullable=False, default=False)

    image = Column(String)

    timestamp = Column(Integer)