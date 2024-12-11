from typing import Annotated
from logging import Logger
from fastapi import status, Depends, APIRouter, Request, Response
from src.core.dep.depedencies_api import InterfaceUnitOfWork, UnitOfWork # noqa
from src.core.dto.portfolio_dto import CreatePortfolio, UserPortfolioInformation # noqa
from src.core.services.portfolio_service import PorfolioService
from src.other.logger import logger_dep, user_config
from src.core.dep.auth.auth_service import AuthService


portfolio_router: APIRouter = APIRouter(
    prefix="/portfolio",
    tags=["Portfolio"]
)


@portfolio_router.post(
    path="/create",
    description="""Создание портфолио""",
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Создание портфолио"
)
async def create_portfolio(
        logger: Annotated[Logger, Depends(logger_dep)],
        uow: Annotated[InterfaceUnitOfWork, Depends(UnitOfWork)],
        user_data: Annotated[dict, Depends(AuthService.verify)],
        description: str,
        req: Request,
        res: Response
) -> None:
    """
    Создание портфолио
    :param logger:
    :param uow:
    :param user_data:
    :param new_portfolio:
    :param req:
    :param res:
    :return:
    """

    logger.info(msg=f"Создание портфолио id = {user_data.get("sub")}", extra=user_config)

    await PorfolioService.create_portfolio(
        token_data=user_data,
        uow=uow,
        new_portfolio=CreatePortfolio(
            id_user=user_data.get('sub'),
            description=description
        ) # noqa
    )


@portfolio_router.get(
    path="/my_portfolio",
    response_model=UserPortfolioInformation,
    description="Информация о моем портфолио",
    summary="Мое портфолио",
    status_code=status.HTTP_200_OK
)
async def my_portfolio(
        logger: Annotated[Logger, Depends(logger_dep)],
        uow: Annotated[InterfaceUnitOfWork, Depends(UnitOfWork)],
        user_data: Annotated[dict, Depends(AuthService.verify)],
        req: Request,
        res: Response
) -> UserPortfolioInformation:
    """
    Информация о моем портфолио
    :param logger:
    :param uow:
    :param user_data:
    :param req:
    :param res:
    :return:
    """

    logger.info(msg=f"Portfolio: Получение информации о своём портфолио id = {user_data.get('sub')}") # noqa

    return await PorfolioService.get_my_portfolio(
        token_data=user_data,
        uow=uow
    )


@portfolio_router.delete(
    path='/delete',
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
    description="""Удаление портфолио""",
    summary="Удаление моего портфолио"
)
async def delete_portfolio(
        logger: Annotated[Logger, Depends(logger_dep)],
        uow: Annotated[InterfaceUnitOfWork, Depends(UnitOfWork)],
        user_data: Annotated[dict, Depends(AuthService.verify)],
        req: Request,
        res: Response
) -> None:
    """
    Удаление портфолио
    :param logger:
    :param uow:
    :param user_data:
    :param req:
    :param res:
    :return:
    """

    logger.info(msg=f"Удаление портфолио id = {user_data.get('sub')}", extra=user_config) # noqa

    await PorfolioService.delete_portfolio(
        token_data=user_data,
        uow=uow
    )
