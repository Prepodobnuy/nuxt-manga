from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from etc.static import DB_URL


def get_engine():
    if not database_exists(DB_URL):
        create_database(DB_URL)
    
    engine = create_engine(DB_URL, pool_size=50, echo=False)
    return engine

def get_engine_from_settings():
    return get_engine()

def get_session(engine = None):
    if engine is None:
        engine = get_engine()
    session = sessionmaker(bind=engine)()
    return session