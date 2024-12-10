from sqlalchemy.ext.asyncio import AsyncSession
from src.databases.postgres.models import UsersType
from src.databases.postgres.repositories import GeneralRepository
from src.databases.postgres.repositories.interfaces.get_all_interface import (
    GetAllInterface,
)  # noqa
from src.databases.postgres.repositories.interfaces.get_one_interface import (
    GetOneInterface,
)  # noqa
from sqlalchemy import select


class UserTypesRepository(GeneralRepository, GetAllInterface, GetOneInterface):
    def __init__(self, model: UsersType, session: AsyncSession) -> None:
        self.__model = model
        self.session = session
        super().__init__(model=self.__model, session=self.session)

    async def get_all(self, _id: int = None):
        """
        Получение всех типов пользователей
        :param _id:
        :return:
        """

        stmt = select(self.__model).where()
        result = (await self.session.execute(stmt)).fetchall()
        return result

    async def get_one(self, _id: int):
        """
        Получение типа пользователя по id
        :param _id:
        :return:
        """

        stmt = select(self.__model).where(self.__model.id == _id)
        result = (await self.session.execute(stmt)).one_or_none()
        return result
