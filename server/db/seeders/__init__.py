import logging

from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemyseeder import ResolvingSeeder

from models import Tag, Genre
from config.db import DATABASE_URL
from .tags import TAGS_DATA
from .genres import GENRES_DATA

logger = logging.getLogger(__name__)


def seed_database():
    logger.debug("seed_database")
    sync_engine = create_engine(DATABASE_URL.replace("+asyncpg", ""))
    Session = sessionmaker(sync_engine)
    session = Session()

    seed_table(en=Tag, session=session, data=TAGS_DATA)
    seed_table(en=Genre, session=session, data=GENRES_DATA)


def seed_table(en, session: Session, data: dict):
    seeder = ResolvingSeeder(session)
    seeder.register_class(en)

    isnone = session.query(en).first() is None

    if isnone:
        logger.info(f"seeding table {en.__tablename__}")
        session.execute(
            text(f"TRUNCATE TABLE {en.__tablename__} RESTART IDENTITY CASCADE;")
        )
        session.commit()

        seeder.load_entities_from_data_dict(data)
        session.commit()
    else:
        logger.info(f"table {en.__tablename__} already seeded")
