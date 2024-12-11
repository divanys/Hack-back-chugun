from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from src.databases.postgres.models import Courses, HobbyCourses
from typing import Sequence, Type
from src.databases.postgres.repositories import GeneralRepository
from src.databases.postgres.repositories.interfaces import DeleteInterface  # noqa
from src.core.errors.courses_errors import CoursesErrors


class CoursesRepository(GeneralRepository, DeleteInterface):
    def __init__(self, session: AsyncSession) -> None:
        self.__model: Type[Courses] = Courses
        self.session = session
        super().__init__(model=self.__model, session=self.session)

    async def get_all(self) -> Sequence:
        """
        Получение всех курсов
        :return:
        """

        stmt = select(Courses, HobbyCourses).outerjoin(HobbyCourses)
        result = await self.session.execute(stmt)
        return result.fetchall()

    async def delete(self, _id: int) -> None:
        """
        Удаление курса
        :param _id:
        :return:
        """

        try:
            stmt = delete(Courses).where(Courses.id == _id)
            await self.session.execute(stmt)
            await self.session.commit()
            return None
        except Exception:
            await CoursesErrors.no_delete_course()
