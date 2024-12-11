from src.core.dep.depedencies_api import InterfaceUnitOfWork
from src.core.dto.portfolio_dto import CreatePortfolio, UserPortfolioInformation, HobbiPortfolio, RecommendsPortfolio
from src.core.errors.auth_errors import AuthErrors
from src.core.errors.portfolio_errors import PortfolioErrors
from src.other.enums.api_enums import UserTypesEnum
from src.databases.postgres.models import Portfolio, UserHobbies, Recommends  # noqa


class PorfolioService:

    @classmethod
    async def create_portfolio(
        cls,
        token_data: dict,
        uow: InterfaceUnitOfWork,
        new_portfolio: CreatePortfolio,  # noqa
    ) -> None:
        """
        Создание портфолио
        :param token_data:
        :param uow:
        :param new_portfolio:
        :return:
        """

        async with uow:
            user_data = await uow.user_repository.get_one(
                _id=token_data.get("sub")
            )  # noqa
            if user_data:
                if user_data[0].id_user_type == UserTypesEnum.USER.value:
                    is_created = await uow.portfolio_repository.create_data(
                        model_data=Portfolio(
                            id_user=new_portfolio.id_user,
                            description=new_portfolio.description,
                        )
                    )

                    if is_created:
                        return
                    await PortfolioErrors.no_create_portfolio()
            await AuthErrors.no_access()

    @classmethod
    async def get_my_portfolio(
        cls, token_data: dict, uow: InterfaceUnitOfWork
    ) -> UserPortfolioInformation:
        """
        Получение портфолио
        :param token_data:
        :param uow:
        :return:
        """

        async with uow:
            user_portfolio = await uow.portfolio_repository.get_one(
                _id=int(token_data.get("sub"))
            )
            user_hobbies = await uow.user_hobbies_repository.get_all(_id=int(token_data.get("sub"))) # noqa
            user_recommends = await uow.recommends_repository.get_all(_id=int(token_data.get("sub"))) # noqa
            if user_portfolio:
                return UserPortfolioInformation(
                    id_user=user_portfolio[0].id,
                    description=user_portfolio[0].description,
                    my_hobbies=[HobbiPortfolio(id_hobby=hobby.id_hobby, id_user=hobby.id_user) for hobby in user_hobbies[0]] if user_hobbies else [], # noqa
                    my_recommends=[RecommendsPortfolio(id_us_ch=rec.id_us_ch, id_user=rec.id_user, description=rec.description) for rec in user_recommends[0]] if user_recommends else [], # noqa
                )
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
            is_deleted = await uow.portfolio_repository.delete(
                _id=int(token_data.get("sub"))
            )
            if is_deleted:
                return None
            await PortfolioErrors.no_delete_portfolio()
