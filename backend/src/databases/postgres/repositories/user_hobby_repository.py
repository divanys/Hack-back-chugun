from src.databases.postgres.models import UserHobbies
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.errors.user_errors import UserErrors
from typing import Type, Sequence
from sqlalchemy import select, delete

from src.databases.postgres.repositories import GeneralRepository
from src.databases.postgres.repositories.interfaces import (
    GetAllInterface,
    DeleteInterface,
)


class UserHobbiesRepository(
    GeneralRepository, GetAllInterface, DeleteInterface
):  # noqa
    def __init__(self, session: AsyncSession) -> None:
        self.__model: Type[UserHobbies] = UserHobbies
        self.session = session
        super().__init__(model=self.__model, session=session)

    async def get_all(self, _id: int) -> Sequence:
        """
        Получение всех пользовательских хобби по id
        :param _id:
        :return:
        """

        stmt = select(UserHobbies).where(UserHobbies.id_user == _id)
        result = await self.session.execute(stmt)
        return result.fetchall()

    async def delete(self, _id: int, id_user: int) -> bool:
        """
        Удаление пользовательского хобби по id
        :param _id:
        :return:
        """

        try:
            stmt = delete(UserHobbies).where(
                UserHobbies.id == _id and UserHobbies.id_user == id_user
            )  # noqa
            await self.session.execute(stmt)
            await self.session.commit()
            return True
        except Exception:
            await UserErrors.no_delete_user_hobby()
