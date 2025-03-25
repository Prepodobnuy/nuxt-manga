from .needed import *
from schemas.person import PersonMetaScheme


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    timestamp = Column(Integer, nullable=False)

    person_meta: Mapped['PersonMeta'] = relationship(back_populates='person')


class PersonMeta(Base):
    """
    Table containing person meta info.
    Needed to give default users ability to suggest changes for current person meta.
    There is can be ONLY ONE public PersonMeta per person.
    """
    __tablename__ = 'person_meta'

    id = Column(Integer, primary_key=True)

    person_id = Column(Integer, ForeignKey('person.id'))
    posted_user_uuid = Column(String, ForeignKey('user.uuid'))

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
    public = Column(Boolean, nullable=False) 

    uhd_cover = Column(String)
    hd_cover = Column(String)
    sd_cover = Column(String)

    person: Mapped['Person'] = relationship(back_populates='person_meta')

    def __init__(self):
        self.timestamp = timestamp()

    def update(self, scheme: PersonMetaScheme):
        self.posted_user_uuid = scheme.posted_user_uuid
        
        self.type = scheme.type
        self.ru_name = scheme.ru_name
        self.en_name = scheme.en_name
        self.or_name = scheme.or_name
        
        self.about = scheme.about

        self.public = False