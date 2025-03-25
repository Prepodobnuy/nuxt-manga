from .needed import *
from schemas.title import TitleMetaScheme
from .stuff import get_by_id
from etc.static import TITLE_PENDING_META_LIMIT


class Title(Base):
    __tablename__ = 'title'
    id = Column(Integer, primary_key=True)
    timestamp = Column(Integer)

    views = Column(Integer, default=0, nullable=False)

    title_meta: Mapped['TitleMeta'] = relationship(back_populates='title')

    def __init__(self) -> None: self.timestamp = timestamp()


class TitleMeta(Base):
    """
    Table containing title meta info.
    Needed to give default users ability to suggest changes for current title meta.
    There is can be ONLY ONE public TitleMeta per title.
    """

    __tablename__ = 'title_meta'
    id = Column(Integer, primary_key=True)
    title_id = Column(Integer, ForeignKey('title.id'))

    posted_user_uuid = Column(String, ForeignKey('user.uuid'))

    ru_name = Column(String, nullable=True)
    en_name = Column(String, nullable=True)
    or_name = Column(String, nullable=True)
    an_name = Column(String, nullable=True)

    description = Column(String, nullable=True)

    # translate status, possible variables: 'translating' 'translated' 'graveyard'
    tr_status = Column(String, nullable=True)
    # release status, possible variables: 'ongoing' 'released' 'paused' 'graveyard'
    rl_status = Column(String, nullable=True)
    # type of the title, possible variables: 'manga', 'manhua'
    title_type = Column(String, nullable=True)

    # age rating, possible variables: '0+' '12+' '16+' '18+'
    age_rating = Column(String, nullable=True)
    # release year, possible variables: 2024, 2001, 1991, etc.
    release_year = Column(Integer, nullable=True)

    # string with tag ids splitted with '/', possible variables: '1/3/2/515/12'
    tags = Column(String, nullable=True)
    # string with genre ids splitted with '/', possible variables: '1/3/2/515/12'
    genres = Column(String, nullable=True)

    timestamp = Column(Integer, nullable=False)

    author_id = Column(Integer, ForeignKey('person.id'), nullable=True)
    artist_id = Column(Integer, ForeignKey('person.id'), nullable=True)
    publisher_id = Column(Integer, ForeignKey('person.id'), nullable=True)

    # key value that responsible for visibility of the metadata
    public = Column(Boolean, nullable=False, default=False)

    uhd_cover = Column(String)
    hd_cover = Column(String)
    sd_cover = Column(String)

    title: Mapped['Title'] = relationship(back_populates='title_meta')

    def __init__(self):
        self.timestamp = timestamp()

    def update(self, scheme: TitleMetaScheme):
        self.posted_user_uuid = scheme.posted_user_uuid
        self.ru_name = scheme.ru_name
        self.en_name = scheme.en_name
        self.or_name = scheme.or_name
        self.an_name = scheme.an_name

        if scheme.tr_status in ['translating', 'translated', 'graveyard']:
            self.tr_status = scheme.tr_status
        if scheme.rl_status in ['ongoing', 'released', 'paused', 'graveyard']:
            self.rl_status = scheme.rl_status
        if scheme.title_type in ['manga', 'manhua']:
            self.title_type = scheme.title_type
        if scheme.age_rating in ['0+', '12+', '16+', '18+']:
            self.age_rating = scheme.age_rating

        self.release_year = scheme.release_year
        self.tags = scheme.tags
        self.genres = scheme.genres
        self.author_id = scheme.author_id
        self.artist_id = scheme.artist_id
        self.publisher_id = scheme.publisher_id

        self.public = False

    @classmethod
    def post_new_meta_new_title(cls, scheme: TitleMetaScheme, uuid: str):
        title = Title()
        meta = TitleMeta()
        meta.update(scheme, uuid)
        meta.title_id = title.id

        try:
            session.add(title)
            session.add(meta)
            session.commit()
            return meta
        except Exception as e:
            session.rollback()
            print(e)
            return None

    @classmethod
    def post_new_meta_existing_title(cls, scheme: TitleMetaScheme, uuid: str):
        if TitleMeta.privat_meta_count() >= TITLE_PENDING_META_LIMIT:
            return None

        title = get_by_id()

        if title is None:
            return None

        meta = TitleMeta()
        meta.update(scheme, uuid)
        meta.title_id = title.id

        try:
            session.add(meta)
            session.commit()
            return meta
        except Exception as e:
            session.rollback()
            print(e)
            return None

    @classmethod
    def privat_meta_count(cls) -> int:
        return cls.privat_meta.len()

    @classmethod
    def privat_meta(cls) -> list["TitleMeta"]:
        return session.query(cls).filter(cls.public == False).all()

    @classmethod
    def delete_public_meta(cls) -> bool:
        meta = session.query(cls).filter(cls.public == True).first()

        if meta is not None:
            try:
                session.delete(meta)
                session.commit()
                return True
            except Exception as e:
                session.rollback()
                print(e)
                return False
        return True

    def to_public(self) -> None:
        if TitleMeta.delete_public_meta():
            self.public = True

    def to_privat(self) -> None:
        self.public = False

    def delete(self) -> bool:
        try:
            session.delete(self)
            session.commit()
            return True
        except Exception as e:
            session.rollback()
            print(e)
            return False
