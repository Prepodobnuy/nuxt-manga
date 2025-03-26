from io import BytesIO

from PIL import Image

from etc.funcs import validate_int
from .needed import Base, timestamp, Session
from .needed import Column, ForeignKey, Integer, String, Boolean
from .needed import Mapped, relationship
from schemas.title import TitleMetaPostScheme
from schemas.title import TitleMetaGetScheme
from etc.static import TITLE_PENDING_META_LIMIT
from .person import Person, PersonMeta
from .rate import TitleRate

from etc.static import ASSETS_DIR
from etc.static import UHD_COVER_GEOMETRY
from etc.static import HD_COVER_GEOMETRY
from etc.static import SD_COVER_GEOMETRY


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

    user_uuid = Column(String, ForeignKey('user.uuid'))

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

    def __init__(
        self,
        title_id: int,
        user_uuid: str,
        ru_name: str,
        en_name: str,
        or_name: str,
        an_name: str,
        tr_status: str,
        rl_status: str,
        title_type: str,
        author_id: int | None,
        artist_id: int | None,
        publisher_id: int | None,
        session: Session,
    ):

        self.title_id = title_id
        self.user_uuid = user_uuid,
        self.ru_name = ru_name
        self.en_name = en_name
        self.or_name = or_name
        self.an_name = an_name
        self.tr_status = tr_status
        self.rl_status = rl_status
        self.title_type = title_type

        if author_id is not None:
            author = session.query(Person).filter(
                Person.id == author_id).first()

            if author is None:
                author_id = None

            author_meta = session.query(PersonMeta).filter(
                PersonMeta.person_id == author_id).filter(PersonMeta.public).first()

            if author_meta is None:
                author_id = None

        if artist_id is not None:
            artist = session.query(Person).filter(
                Person.id == artist_id).first()

            if artist is None:
                artist_id = None

            artist_meta = session.query(PersonMeta).filter(
                PersonMeta.person_id == artist_id).filter(PersonMeta.public).first()

            if artist_meta is None:
                artist_id = None

        if publisher_id is not None:
            publisher = session.query(Person).filter(
                Person.id == publisher_id).first()

            if publisher is None:
                publisher_id = None

            publisher_meta = session.query(PersonMeta).filter(
                PersonMeta.person_id == publisher_id).filter(PersonMeta.public).first()

            if publisher_meta is None:
                publisher_id = None

        self.author_id = author_id
        self.artist_id = artist_id
        self.publisher_id = publisher_id

    @classmethod
    def new(cls, session: Session, scheme: TitleMetaPostScheme, uuid: str) -> "TitleMeta":
        if len(session.query(TitleMeta).filter(TitleMeta.public is False).all()) >= TITLE_PENDING_META_LIMIT:
            return None

        title = session.query(Title).filter(Title.id == scheme.id).first()

        if scheme.title_id is None or title is None:
            title = Title()
            try:
                session.add(title)
                session.commit()
            except Exception:
                session.rollback()
                return None

        meta = TitleMeta(
            title_id=title.id,
            user_uuid=uuid,
            ru_name=scheme.ru_name,
            en_name=scheme.en_name,
            or_name=scheme.or_name,
            an_name=scheme.an_name,
            tr_status=scheme.tr_status,
            rl_status=scheme.rl_status,
            title_type=scheme.title_type,
            author_id=scheme.author_id,
            artist_id=scheme.artist_id,
            publisher_id=scheme.publisher_id,
            session=session,
        )

        return meta

    def get(self, session: Session, uuid: str | None) -> TitleMetaGetScheme:
        return TitleMetaGetScheme(
            id=self.id,
            title_id=self.title_id,
            user_uuid=self.user_uuid,
            ru_name=self.ru_name,
            en_name=self.en_name,
            or_name=self.or_name,
            an_name=self.an_name,
            tr_status=self.tr_status,
            rl_status=self.rl_status,
            title_type=self.title_type,
            age_rating=self.age_rating,
            release_year=self.release_year,
            tags=self.tags,
            genres=self.genres,
            timestamp=self.timestamp,
            author_id=self.author_id,
            artist_id=self.artist_id,
            publisher_id=self.publisher_id,
            public=self.public,
            rates_1=len(get_rates(session, self.title_id, 1)),
            rates_2=len(get_rates(session, self.title_id, 2)),
            rates_3=len(get_rates(session, self.title_id, 3)),
            rates_4=len(get_rates(session, self.title_id, 4)),
            rates_5=len(get_rates(session, self.title_id, 5)),
            rates_6=len(get_rates(session, self.title_id, 6)),
            rates_7=len(get_rates(session, self.title_id, 7)),
            rates_8=len(get_rates(session, self.title_id, 8)),
            rates_9=len(get_rates(session, self.title_id, 9)),
            rates_10=len(get_rates(session, self.title_id, 10)),
            rated_value=get_rated(session, uuid),
        )

    def set_cover(self, bytes: BytesIO):
        uhd_path = f'{ASSETS_DIR}/{self.title_id}-{self.id}uhd'
        hd_path = f'{ASSETS_DIR}/{self.title_id}-{self.id}hd'
        sd_path = f'{ASSETS_DIR}/{self.title_id}-{self.id}sd'

        try:
            with Image.open(bytes) as image:
                image = image.resize(UHD_COVER_GEOMETRY,
                                     Image.Resampling.BILINEAR)
                image.save(uhd_path)
                image = image.resize(
                    HD_COVER_GEOMETRY, Image.Resampling.BILINEAR)
                image.save(hd_path)
                image = image.resize(
                    SD_COVER_GEOMETRY, Image.Resampling.BILINEAR)
                image.save(sd_path)

            self.uhd_path = uhd_path
            self.hd_path = hd_path
            self.sd_path = sd_path
        except Exception as e:
            ...


def get_rates(session: Session, title_id: int, rate_value: int) -> list[int]:
    return session.query(TitleRate).filter(TitleRate.title_id == title_id).filter(TitleRate.rate == rate_value).all()


def get_rated(session: Session, uuid: str | None) -> int | None:
    if uuid is None:
        return None

    rate = session.query(TitleRate).filter(TitleRate.user_uuid == uuid).first()

    if rate is None:
        return None

    return validate_int(rate.rate, 1, 10)
