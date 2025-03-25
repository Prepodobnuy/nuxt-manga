import uuid
import time

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship, Mapped, Session
from sqlalchemy.exc import NoResultFound

from database import session
from config import hash_string

Base = declarative_base()

def timestamp() -> int: return int(time.time())

def uuid4() -> str: return str(uuid.uuid4())