from sqlalchemy.ext.asyncio import AsyncSession

from src.databases.postgres.models import Vacancies
from src.databases.postgres.repositories import GeneralRepository
from src.databases.postgres.repositories.interfaces.get_all_interface import (
    GetAllInterface,
)  # noqa
from src.databases.postgres.repositories.interfaces.update_interface import (
    UpdateInterface,
)  # noqa
from src.databases.postgres.repositories.interfaces.delete_interface import (
    DeleteInterface,
)  # noqa
from sqlalchemy import select, delete, update
from typing import Type, Sequence


class VacanciesRepository(
    GeneralRepository,
    GetAllInterface,
    UpdateInterface,
    DeleteInterface,
):
    def __init__(self, session: AsyncSession) -> None:
        self.__model: Type[Vacancies] = Vacancies
        self.session = session
        super().__init__(model=self.__model, session=self.session)

    async def get_all(self, _id: int):
        """
        Получение всех пользователей
        :param _id:
        :return:
        """

        stmt = select(self.__model).where(self.__model.id_user == int(_id))
        result = (await self.session.execute(stmt)).fetchall()
        return result

    async def delete(self, _id: int) -> bool:
        """
        Удаление пользователя по идентификатору
        :param _id:
        :return:
        """

        stmt = delete(self.__model).where(self.__model.id == int(_id))
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result

    async def update_one(self, _id: int, data: dict) -> None:
        """
        Обновление пользовательской информации
        :param _id:
        :param data:
        :return:
        """

        stmt = (
            update(self.__model).where(self.__model.id == int(_id)).values(data)
        )  # noqa
        result = await self.session.execute(stmt)
        await self.session.commit()
        if result:
            return True
        return False

    async def find_all_vacancies(self) -> Sequence:
        """
        Все вакансии
        :return:
        """

        stmt = select(self.__model)
        result = await self.session.execute(stmt)
        return result.all()
