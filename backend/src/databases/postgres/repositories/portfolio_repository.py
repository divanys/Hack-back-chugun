from sqlalchemy.ext.asyncio import AsyncSession
from src.databases.postgres.models import Portfolio
from src.databases.postgres.repositories import GeneralRepository  # noqa
from src.databases.postgres.repositories.interfaces import (
    DeleteInterface,
    GetOneInterface,
)  # noqa
from sqlalchemy import select, delete
from typing import Type, Sequence
from src.core.errors.portfolio_errors import PortfolioErrors


class PortfolioRepository(GeneralRepository, DeleteInterface, GetOneInterface):  # noqa
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        self.__model: Type[Portfolio] = Portfolio
        super().__init__(model=self.__model, session=self.session)

    async def get_one(self, _id: int) -> Sequence:
        """
        Получение портфолио по id user
        :param _id:
        :return:
        """

        stmt = select(Portfolio).where(Portfolio.id_user == _id)
        result = await self.session.execute(stmt)
        return result.one_or_none()

    async def delete(self, _id: int) -> None:
        """
        Удаление портфолио по id user
        :param _id:
        :return:
        """

        try:
            stmt = delete(Portfolio).where(Portfolio.id_user == _id)
            await self.session.execute(stmt)
            await self.session.commit()
            return True
        except Exception:
            await PortfolioErrors.no_delete_portfolio()
