from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from config.db import DATABASE_URL

engine = create_async_engine(
    url=DATABASE_URL, future=True, pool_size=10, max_overflow=20, pool_recycle=3600
)

async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


def connection(method):
    async def wrapper(*args, **kwargs):
        if "session" in kwargs and kwargs["session"] is not None:
            return await method(*args, **kwargs)

        async with async_session_maker() as session:
            try:
                return await method(*args, session=session, **kwargs)
            except Exception as e:
                await session.rollback()
                raise e
            finally:
                await session.close()

    return wrapper


async def get_session() -> AsyncGenerator[AsyncSession]:
    async with async_session_maker() as session:
        yield session
