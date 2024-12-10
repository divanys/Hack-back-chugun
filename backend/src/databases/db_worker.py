from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
)
from backend.configs import db


class DatabaseWorker:

    def __init__(self) -> None:
        self.__engine: AsyncEngine = create_async_engine(
            url=f"postgresql+asyncpg://{db.DB_USER}:{db.DB_PASSWORD}@{db.DB_HOST}:{db.DB_PORT}/{db.REDIS_PORT}"  # noqa
        )
        self.__session = async_sessionmaker(
            bind=self.__engine, class_=AsyncSession
        )  # noqa

    @property
    async def session(self) -> async_sessionmaker[AsyncSession]:
        return self.__session
