from io import BytesIO

from PIL import Image

from .needed import Base, relationship, Mapped, Integer, String, Boolean, Column, ForeignKey, timestamp, Session
from schemas.person import PersonMetaGetScheme
from schemas.person import PersonMetaPostScheme
from etc.static import PERSON_PENDING_META_LIMIT
from etc.static import ASSETS_DIR
from etc.static import UHD_COVER_GEOMETRY
from etc.static import HD_COVER_GEOMETRY
from etc.static import SD_COVER_GEOMETRY


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    timestamp = Column(Integer, nullable=False)

    person_meta: Mapped['PersonMeta'] = relationship(back_populates='person')

    def __init__(self): self.timestamp = timestamp()


class PersonMeta(Base):
    """
    Table containing person meta info.
    Needed to give default users ability to suggest changes for current person meta.
    There is can be ONLY ONE public PersonMeta per person.
    """
    __tablename__ = 'person_meta'

    id = Column(Integer, primary_key=True)

    person_id = Column(Integer, ForeignKey('person.id'))
    user_uuid = Column(String, ForeignKey('user.uuid'))

    # type of person
    type = Column(String, nullable=True)
    # person name in russian
    ru_name = Column(String, nullable=True)
    # person name in engish
    en_name = Column(String, nullable=True)
    # person name in the language of original
    or_name = Column(String, nullable=True)

    # information about person
    about = Column(String, nullable=True)

    # key value that responsible for visibility of the metadata
    public = Column(Boolean, nullable=False, default=False)

    uhd_cover = Column(String)
    hd_cover = Column(String)
    sd_cover = Column(String)

    person: Mapped['Person'] = relationship(back_populates='person_meta')

    def __init__(
        self,
        person_id: int,
        type: str,
        ru_name: str,
        en_name: str,
        or_name: str,
        about: str,
        user_uuid: str,
    ):
        self.user_uuid = user_uuid
        self.timestamp = timestamp()
        self.person_id = person_id
        self.type = type
        self.ru_name = ru_name
        self.en_name = en_name
        self.or_name = or_name
        self.about = about
        self.public = False

    def set_cover(self, bytes: BytesIO):
        uhd_path = f'{ASSETS_DIR}/person{self.person_id}-{self.id}uhd'
        hd_path = f'{ASSETS_DIR}/person{self.person_id}-{self.id}hd'
        sd_path = f'{ASSETS_DIR}/person{self.person_id}-{self.id}sd'

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

    def get(self, session: Session) -> PersonMetaGetScheme:
        return PersonMetaGetScheme(
            id=self.id,
            person_id=self.person_id,
            posted_user_uuid=self.posted_user_uuid,
            type=self.type,
            ru_name=self.ru_name,
            en_name=self.en_name,
            or_name=self.or_name,
            about=self.about,
            timestamp=self.timestamp,
            public=self.public,
        )

    @classmethod
    def new(cls, session: Session, scheme: PersonMetaPostScheme, uuid: str) -> "PersonMeta":
        if scheme.person_id is None:
            person = Person()
            try:
                session.add(person)
                session.commit()
            except Exception as e:
                print(e)
                session.rollback()
                return
        else:
            person = session.query(Person.id == scheme.person_id).first()
            if person is None:
                person = Person()
                try:
                    session.add(person)
                    session.commit()
                except Exception as e:
                    print(e)
                    session.rollback()
                    return

        pending_meta_length = len(session.query(PersonMeta).filter(
            PersonMeta.person_id == person.id).all())

        if pending_meta_length >= PERSON_PENDING_META_LIMIT:
            return None

        return PersonMeta(
            person_id=scheme.person_id,
            type=scheme.type,
            ru_name=scheme.ru_name,
            en_name=scheme.en_name,
            or_name=scheme.or_name,
            about=scheme.about,
            user_uuid=uuid,
        )
