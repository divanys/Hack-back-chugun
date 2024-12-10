from logging import Logger
from typing import Annotated

from fastapi import APIRouter, Depends, status, Request, Response
from src.other import logger_dep, user_config
from src.core.dto import RegisterUser, AuthUser
from src.core.dep.depedencies_api import UnitOfWork, InterfaceUnitOfWork
from src.core.services.user_service import UserService


auth_router: APIRouter = APIRouter(prefix="/auth", tags=["Auth"])


@auth_router.post(
    path="/register",
    description="""
    Регистрация пользователя
    """,
    summary="Регистрация пользователя",
    response_model=None,
    status_code=status.HTTP_201_CREATED,
)
async def registration_user(
    user_data: RegisterUser,
    logger: Annotated[Logger, Depends(logger_dep)],
    db: Annotated[InterfaceUnitOfWork, Depends(UnitOfWork)],
) -> None:
    """
    APIROUTER - Регистрация пользователя
    :param user_data:
    :param logger:
    :return:
    """

    logger.info(
        msg=f"AUTH: Регистрация пользователя email={user_data.email}",
        extra=user_config,  # noqa
    )  # noqa
    await UserService.register_user_on_db(uow=db, user_data=user_data)


@auth_router.post(
    path="/login",
    description="""
    Авторизация пользователя
    """,
    summary="Авторизация",
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
)
async def login_user(
    logger: Annotated[Logger, Depends(logger_dep)],
    db: Annotated[InterfaceUnitOfWork, Depends(UnitOfWork)],
    user_data: AuthUser,
    req: Request,
    res: Response,
) -> None:
    """
    APIRouter - Авторизация пользователя
    :param logger:
    :param db:
    :param user_data:
    :return:
    """

    logger.info(
        msg=f"AUTH: Авторизация пользователя email={user_data.email}",
        extra=user_config,  # noqa
    )

    await UserService.login_user(uow=db, user_data=user_data, res=res)
