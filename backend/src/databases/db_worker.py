from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, declared_attr
from backend.configs import db


class DatabaseWorker:

    def __init__(self) -> None:
        self.__engine: AsyncEngine = create_async_engine(
            url=""
        )
