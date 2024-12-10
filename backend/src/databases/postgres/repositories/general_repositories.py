from typing import Union
from src.databases.postgres.models import (  # noqa
    UsersType,
    Users,
    University,
    Recommends,
    Hobbies,
    Courses,
    Vacancies,
    HobbyCourses,
    UserHobbies,
    Portfolio,
    Tasks,
)
from sqlalchemy.ext.asyncio import AsyncSession
from src.databases.postgres.repositories.interfaces import CreateInterface
from sqlalchemy import insert


class GeneralRepository(CreateInterface):

    def __init__(
        self,
        model: Union[
            Users,
            UsersType,
            Hobbies,
            HobbyCourses,
            UserHobbies,
            Vacancies,
            University,
            Portfolio,
            Tasks,
            Courses,
            Recommends,
        ],
        session: AsyncSession,
    ) -> None:
        self.__model = model
        self.session = session

    async def create_data(self, model_data) -> bool:
        """
        Создание записи
        :param args:
        :return:
        """

        stmt = insert(self.__model).values(await model_data.read_model())
        result = await self.session.execute(stmt)
        if result:
            await self.session.commit()
            return True
        return False
