from src.core.dep.depedencies_api import InterfaceUnitOfWork
from src.databases.postgres.repositories import (  # noqa
    UserRepository,
    UserTypesRepository,
)  # noqa
from sqlalchemy.ext.asyncio import AsyncSession
from src.databases.db_worker import DatabaseWorker


class UnitOfWork(InterfaceUnitOfWork):

    def __init__(self):
        self.database_worker: DatabaseWorker = DatabaseWorker()

    async def __aenter__(self):
        """
        Получаем сессию
        :return:
        """

        async with self.database_worker.session() as session:
            self.session: AsyncSession = session
            self.user_repository = UserRepository(session=self.session)  # noqa
            self.user_type_repository = UserTypesRepository(
                session=self.session
            )  # noqa

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """
        Закрытие сессии
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """

        if exc_type:
            self.session.rollback()
        self.session.close()

    async def commit(self):
        """
        Коммит сессии
        :return:
        """

        self.session.commit()
