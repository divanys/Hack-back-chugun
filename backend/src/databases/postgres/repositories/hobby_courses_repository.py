from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from src.databases.postgres.models import HobbyCourses
from typing import Sequence, Type
from src.databases.postgres.repositories import GeneralRepository
from src.databases.postgres.repositories.interfaces import (
    DeleteInterface,
    GetAllInterface,
)  # noqa
from src.core.errors.hobby_course_errors import HobbyCoursesErrors  # noqa


class HobbyCoursesRepository(
    GeneralRepository, DeleteInterface, GetAllInterface
):  # noqa
    def __init__(self, session: AsyncSession) -> None:
        self.__model: Type[HobbyCourses] = HobbyCourses
        self.session = session
        super().__init__(model=self.__model, session=self.session)

    async def get_all(self, _id: int) -> Sequence:
        """
        Получение всех курсов
        :return:
        """

        stmt = select(HobbyCourses).where(HobbyCourses.id_course == _id)
        result = await self.session.execute(stmt)
        return result.fetchall()

    async def delete(self, _id: int) -> None:
        """
        Удаление курса
        :param _id:
        :return:
        """

        try:
            stmt = delete(HobbyCourses).where(HobbyCourses.id == _id)
            await self.session.execute(stmt)
            await self.session.commit()
            return None
        except Exception:
            await HobbyCoursesErrors.no_delete_hobby_courses()
