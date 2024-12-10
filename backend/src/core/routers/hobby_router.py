from logging import Logger
from sys import prefix

from fastapi import APIRouter, Depends, status
from fastapi.responses import Response
from fastapi.requests import Request

from src.core.dep.auth.auth_service import AuthService
from src.core.dep.depedencies_api import InterfaceUnitOfWork, UnitOfWork  # noqa
from typing import Annotated
from src.core.services.hobby_service import HobbyService
from src.other import logger_dep, user_config
from src.core.dto.hobby_dto import CreateHobby, AllHobbies


hobby_router: APIRouter = APIRouter(
    prefix="/hobby",
    tags=["Hobby"]
)


@hobby_router.post(
    path='/create',
    description="Создание хобби, доступен для администратора",
    summary="Создание хобби",
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT
)
async def create_hobby(
        logger: Annotated[Logger, Depends(logger_dep)],
        db: Annotated[InterfaceUnitOfWork, Depends(UnitOfWork)],
        token_data: Annotated[dict, Depends(AuthService.verify)],
        new_hobby: CreateHobby,
        req: Request,
        res: Response
) -> None:
    """
    Создание хобби
    :param logger:
    :param db:
    :param token_data:
    :param new_hobby:
    :return:
    """

    logger.info(msg=f"Hobbies: Создание хобби {new_hobby.dict()}", extra=user_config)

    await HobbyService.create(
        uow=db,
        token_data=token_data,
        new_hobby=new_hobby
    )

@hobby_router.get(
    path="/all_hobbies",
    response_model=AllHobbies,
    description="Все хобби",
    summary="Все хобби",
    status_code=status.HTTP_200_OK
)
async def all_hobbies(
        logger: Annotated[Logger, Depends(logger_dep)],
        db: Annotated[InterfaceUnitOfWork, Depends(UnitOfWork)],
        req: Request,
        res: Response
) -> AllHobbies:
    """
    Все хобби
    :param logger:
    :param db:
    :param req:
    :param res:
    :return:
    """

    logger.info(msg=f"Hobbies: Получение всех хобби", extra=user_config)

    return await HobbyService.all_hobby(uow=db)


@hobby_router.delete(
    path="/delete",
    description="""
    Удаление хобби. Доступно только для администратора
    """,
    summary="Удаление хобби",
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_hobby(
        logger: Annotated[Logger, Depends(logger_dep)],
        db: Annotated[InterfaceUnitOfWork, Depends(UnitOfWork)],
        token_data: Annotated[dict, Depends(AuthService.verify)],
        id_hobby: int,
        req: Request,
        res: Response
) -> None:
    """
    Удаление хобби
    :param logger:
    :param db:
    :param token_data:
    :param id_hobby:
    :param req:
    :param res:
    :return:
    """

    await HobbyService.delete_hobby(
        uow=db,
        token_data=token_data,
        id_hobby=id_hobby
    )