from src.core.dep.depedencies_api import InterfaceUnitOfWork
from src.core.dto.portfolio_dto import CreatePortfolio, UserPortfolioInformation
from src.core.errors.auth_errors import AuthErrors
from src.core.errors.portfolio_errors import PortfolioErrors
from src.other.enums.api_enums import UserTypesEnum
from src.databases.postgres.models import Portfolio, UserHobbies, Recommends # noqa


class PorfolioService:

    @classmethod
    async def create_portfolio(
            cls,
            token_data: dict,
            uow: InterfaceUnitOfWork,
            new_portfolio: CreatePortfolio
    ) -> None:
        """
        Создание портфолио
        :param token_data:
        :param uow:
        :param new_portfolio:
        :return:
        """

        async with uow:
            user_data = await uow.user_repository.get_one(_id=token_data.get("sub"))
            if user_data:
                if user_data[0].id_user_type == UserTypesEnum.USER.value:
                    is_created = await uow.portfolio_repository.create_data(
                        model_data=Portfolio(
                            id_user=new_portfolio.id_user,
                            description=new_portfolio.description
                        )
                    )

                    if is_created:
                        return
                    await PortfolioErrors.no_create_portfolio()
            await AuthErrors.no_access()

    @classmethod
    async def get_my_portfolio(
            cls,
            token_data: dict,
            uow: InterfaceUnitOfWork
    ) -> UserPortfolioInformation:
        """
        Получение портфолио
        :param token_data:
        :param uow:
        :return:
        """

        async with uow:
            user_portfolio = await uow.portfolio_repository.get_one(_id=token_data.get("sub"))
            if user_portfolio:
                pass
                return UserPortfolioInformation()
            await PortfolioErrors.no_found_portfolio()

    @classmethod
    async def delete_portfolio(
            cls,
            token_data: dict,
            uow: InterfaceUnitOfWork,
    ) -> None:
        """
        Удаление портфолио
        :param token_data:
        :param uow:
        :return:
        """

        async with uow:
            is_deleted = await uow.portfolio_repository.delete(_id=int(token_data.get("sub")))
            if is_deleted:
                return None
            await PortfolioErrors.no_delete_portfolio()
