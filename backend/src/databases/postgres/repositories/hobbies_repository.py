from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from src.databases.postgres.models import Hobbies
from typing import Sequence, Type
from src.databases.postgres.repositories import GeneralRepository
from src.core.errors.hobby_course_errors import HobbyCoursesErrors
from src.databases.postgres.repositories.interfaces import DeleteInterface  # noqa


class HobbiesRepository(GeneralRepository, DeleteInterface):
    def __init__(self, session: AsyncSession) -> None:
        self.__model: Type[Hobbies] = Hobbies
        self.session = session
        super().__init__(model=self.__model, session=self.session)

    async def get_all(self) -> Sequence:
        """
        Получение всех курсов
        :return:
        """

        stmt = select(Hobbies)
        result = await self.session.execute(stmt)
        return result.fetchall()

    async def delete(self, _id: int) -> None:
        """
        Удаление курса
        :param _id:
        :return:
        """

        try:
            stmt = delete(Hobbies).where(Hobbies.id == _id)
            await self.session.execute(stmt)
            await self.session.commit()
            return None
        except Exception:
            await HobbyCoursesErrors.no_delete_hobby()
