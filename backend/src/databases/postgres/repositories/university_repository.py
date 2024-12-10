from src.databases.postgres.models.university import University
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from src.databases.postgres.repositories import GeneralRepository
from src.databases.postgres.repositories.interfaces import (
    GetOneInterface,
    DeleteInterface,
)
from typing import Type, Sequence
from src.core.errors.university_errors import UniversityErrors


class UniversityRepository(GeneralRepository, GetOneInterface, DeleteInterface):  # noqa

    def __init__(self, session: AsyncSession) -> None:
        self.__model: Type[University] = University
        self.session = session
        super().__init__(model=self.__model, session=self.session)

    async def get_all(self) -> Sequence:
        """
        Получение всех заведений
        :param _id:
        :return:
        """

        stmt = select(University)
        result = await self.session.execute(stmt)
        return result.fetchall()

    async def get_one(self, _id: int) -> None:
        """
        Поиск заведения по id
        :param _id:
        :return:
        """

        stmt = select(University).where(University.id == _id)
        result = await self.session.execute(stmt)
        return result.one_or_none()

    async def delete(self, _id: int) -> None:
        """
        Удаление заведения по id
        :param _id:
        :return:
        """

        try:
            stmt = delete(University).where(University.id == _id)
            await self.session.execute(stmt)
            await self.session.commit()
            return None
        except Exception:
            await UniversityErrors.no_delete_university()
