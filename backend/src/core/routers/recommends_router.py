from typing import Annotated
from logging import Logger
from fastapi import status, Depends, APIRouter, Request, Response
from src.core.dep.depedencies_api import InterfaceUnitOfWork, UnitOfWork  # noqa
from src.core.dto.recommends_dto import CreateRecommends, AllUserRecommends
from src.core.services.recommends_service import RecommendsService
from src.other.logger import logger_dep, user_config
from src.core.dep.auth.auth_service import AuthService


rec_router: APIRouter = APIRouter(prefix="/recommends", tags=["Recommends"])  # noqa


@rec_router.post(
    path="/create",
    description="""Создание рекомендации""",
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Создание рекомендации",
)
async def create_portfolio(
    logger: Annotated[Logger, Depends(logger_dep)],
    uow: Annotated[InterfaceUnitOfWork, Depends(UnitOfWork)],
    user_data: Annotated[dict, Depends(AuthService.verify)],
    id_user: int,
    description: str,
    req: Request,
    res: Response,
) -> None:
    """
    Создание Рекомендации
    :param logger:
    :param uow:
    :param user_data:
    :param new_portfolio:
    :param req:
    :param res:
    :return:
    """

    logger.info(
        msg=f"Создание рекомендации id = {user_data.get("sub")}",
        extra=user_config,  # noqa
    )

    await RecommendsService.create_recommends(
        token_data=user_data,
        uow=uow,
        new_rec=CreateRecommends(
            id_user=id_user,
            id_us_ch=int(user_data.get("sub")),
            description=description,  # noqa
        ),
    )


@rec_router.get(
    path="/my_recommends",
    response_model=AllUserRecommends,
    description="Все пользовательские рекомендации",
    summary="Мои рекомендации",
    status_code=status.HTTP_200_OK,
)
async def my_portfolio(
    logger: Annotated[Logger, Depends(logger_dep)],
    uow: Annotated[InterfaceUnitOfWork, Depends(UnitOfWork)],
    user_data: Annotated[dict, Depends(AuthService.verify)],
    req: Request,
    res: Response,
) -> AllUserRecommends:
    """
    Все пользовательские рекомендации
    :param logger:
    :param uow:
    :param user_data:
    :param req:
    :param res:
    :return:
    """

    logger.info(
        msg=f"Recommends: Получение информации о своих рекомендациях id = {user_data.get('sub')}"  # noqa
    )  # noqa

    return await RecommendsService.get_my_recommends(
        token_data=user_data, uow=uow
    )  # noqa


@rec_router.delete(
    path="/delete",
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
    description="""Удаление рекомендации""",
    summary="Удаление моей рекомендации",
)
async def delete_portfolio(
    logger: Annotated[Logger, Depends(logger_dep)],
    uow: Annotated[InterfaceUnitOfWork, Depends(UnitOfWork)],
    user_data: Annotated[dict, Depends(AuthService.verify)],
    id_rec: int,
    req: Request,
    res: Response,
) -> None:
    """
    Удаление рекомендации
    :param logger:
    :param uow:
    :param user_data:
    :param req:
    :param res:
    :return:
    """

    logger.info(
        msg=f"Удаление рекомендации id = {user_data.get('sub')}",
        extra=user_config,  # noqa
    )  # noqa

    await RecommendsService.delete_recommends(
        token_data=user_data, uow=uow, id_rec=id_rec
    )
