import asyncio
import logging

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


from config.logger import LOGGER_FILENAME, LOGGER_LEVEL
from db.seeders import seed_database
from db.session_fabric import connection
from models import create_metadata
from models.person.person import Person
from models.person.personmeta import PersonMeta
from models.user.user import User
from modules.permission.roles import Role
from routes import run

logger = logging.getLogger(__name__)


@connection
async def test(
    session: AsyncSession | None = None,
):
    assert session is not None

    exec = await session.execute(select(Person))
    p = exec.scalars().all()
    exec = await session.execute(select(PersonMeta))
    aa = exec.scalars().all()

    for pp in aa:
        await session.delete(pp)

    await session.flush()

    for a in p:
        await session.delete(a)

    await session.commit()


def main():
    logging.basicConfig(filename=LOGGER_FILENAME, level=LOGGER_LEVEL)
    logger.debug("main")
    create_metadata()
    seed_database()
    run()


if __name__ == "__main__":
    main()
    # asyncio.run(test())
