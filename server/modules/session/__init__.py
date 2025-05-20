from typing import Callable
from sqlalchemy import exc
from sqlalchemy.ext.asyncio import AsyncSession
from db.session_fabric import connection


class SessionHelper:
    @connection
    @staticmethod
    async def add(en, session: AsyncSession):
        try:
            session.add(en)
            await session.commit()
        except Exception as e:
            await session.rollback()
            raise e

    @connection
    @staticmethod
    async def add_list(en: list, session: AsyncSession):
        try:
            for e in en:
                session.add(e)
            await session.commit()
        except Exception as e:
            await session.rollback()
            raise e

    @connection
    @staticmethod
    async def delete(en, session: AsyncSession):
        try:
            await session.delete(en)
            await session.commit()
        except Exception as e:
            await session.rollback()
            raise e

    @connection
    @staticmethod
    async def delete_list(en: list, session: AsyncSession):
        try:
            for e in en:
                await session.delete(e)
            await session.commit()
        except Exception as e:
            await session.rollback()
            raise e

    @connection
    @staticmethod
    async def execute(call: Callable, session: AsyncSession):
        try:
            call()
            await session.commit()
        except Exception as e:
            await session.rollback()
            raise e
