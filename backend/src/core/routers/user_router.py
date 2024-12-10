from logging import Logger
from typing import Annotated

from fastapi import APIRouter, Depends, status
from src.other import logger_dep, user_config
from src.core.dto import RegisterUser
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
