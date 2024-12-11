from sqlalchemy.ext.asyncio import AsyncSession
from src.databases.postgres.models import Recommends
from src.databases.postgres.repositories import GeneralRepository  # noqa
from src.databases.postgres.repositories.interfaces import (
    DeleteInterface,
    GetAllInterface,
)  # noqa
from sqlalchemy import select, delete
from typing import Type, Sequence
from src.core.errors.recommends_errors import RecommendsErrors


class RecommendsRepository(GeneralRepository, DeleteInterface, GetAllInterface):  # noqa
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        self.__model: Type[Recommends] = Recommends
        super().__init__(model=self.__model, session=self.session)

    async def get_all(self, _id: int) -> Sequence:
        """
        Получение всех рекомендаций пользоватедя
        :param _id:
        :return:
        """

        stmt = select(Recommends).where(Recommends.id_user == _id)
        result = await self.session.execute(stmt)
        return result.all()

    async def delete(self, _id: int) -> None:
        """
        Удаление рекомендации по id
        :param _id:
        :return:
        """

        try:
            stmt = delete(Recommends).where(Recommends.id == _id)
            await self.session.execute(stmt)
            await self.session.commit()
            return True
        except Exception:
            await RecommendsErrors.no_delete_recommends()
