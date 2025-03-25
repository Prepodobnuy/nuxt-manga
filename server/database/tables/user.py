from io import BytesIO

from PIL import Image

from .needed import *
from etc.role import ROLE_USER
from schemas.auth import Credentials
from schemas.user import UserPublicScheme
from etc.static import ASSETS_DIR
from etc.static import UHD_PFP_GEOMETRY
from etc.static import HD_PFP_GEOMETRY
from etc.static import SD_PFP_GEOMETRY


class User(Base):
    __tablename__ = 'user'

    uuid = Column(String, primary_key=True)    
    username = Column(String)
    email = Column(String)
    hashed_password = Column(String)
    role = Column(String)

    hide_username = Column(Boolean, default=False)
    hide_email = Column(Boolean, default=False)

    nickname = Column(String)
    status = Column(String)
    about = Column(String)

    timestamp = Column(Integer, nullable=False)

    uhd_path = Column(String)
    hd_path = Column(String)
    sd_path = Column(String)

    def __init__(self, credentials: Credentials):
        self.uuid = uuid4()
        self.username = credentials.username
        self.email = credentials.email
        self.hashed_password = hash_string(credentials.password)
        self.role = ROLE_USER

        self.hide_username = False
        self.hide_email = False

        self.nickname = credentials.username
        self.status = ''
        self.about = ''

        self.timestamp = timestamp()

    def public_scheme(self) -> UserPublicScheme:
        return UserPublicScheme(
            username=self.username if not self.hide_username else None,
            email=self.email if not self.email else None,
            uuid=self.uuid,
            nickname=self.nickname,
            status=self.status,
            about=self.about,
        )
    
    def set_pfp(self, bytes: BytesIO):
        uhd_path = f'{ASSETS_DIR}/{self.uuid}uhd'
        hd_path = f'{ASSETS_DIR}/{self.uuid}hd'
        sd_path = f'{ASSETS_DIR}/{self.uuid}sd'

        try:
            with Image.open(bytes) as image:
                image = image.resize(UHD_PFP_GEOMETRY, Image.Resampling.BILINEAR)
                image.save(uhd_path)
                image = image.resize(HD_PFP_GEOMETRY, Image.Resampling.BILINEAR)
                image.save(hd_path)
                image = image.resize(SD_PFP_GEOMETRY, Image.Resampling.BILINEAR)
                image.save(sd_path)
            
            self.uhd_path = uhd_path
            self.hd_path = hd_path
            self.sd_path = sd_path
        except Exception as e:...

    def password_matches(self, new_password: str) -> bool:
        return self.hashed_password == hash_string(new_password)

    @classmethod
    def get_by_username(cls, session: Session, username: str):
        return session.query(cls).filter(cls.username == username).first()
    
    @classmethod
    def get_by_uuid(cls, session: Session, uuid: str):
        return session.query(cls).filter(cls.uuid == uuid).first()