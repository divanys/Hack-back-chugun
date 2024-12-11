from logging import Logger
from fastapi import APIRouter, Depends, status
from fastapi.responses import Response
from fastapi.requests import Request

from src.core.dep.auth.auth_service import AuthService
from src.core.dep.depedencies_api import InterfaceUnitOfWork, UnitOfWork  # noqa
from typing import Annotated

from src.core.dto.user_dto import AddUserHobby, UserHobbies
from src.core.services.hobby_service import HobbyService
from src.core.services.user_hobbies_service import UserHobbiesService
from src.other import logger_dep, user_config
from src.core.dto.hobby_dto import CreateHobby, AllHobbies


hobby_router: APIRouter = APIRouter(prefix="/hobby", tags=["Hobby"])  # noqa


@hobby_router.post(
    path="/create",
    description="Создание хобби, доступен для администратора",
    summary="Создание хобби",
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
)
async def create_hobby(
    logger: Annotated[Logger, Depends(logger_dep)],
    db: Annotated[InterfaceUnitOfWork, Depends(UnitOfWork)],  # noqa
    token_data: Annotated[dict, Depends(AuthService.verify)],  # noqa
    new_hobby: CreateHobby,
    req: Request,
    res: Response,
) -> None:
    """
    Создание хобби
    :param logger:
    :param db:
    :param token_data:
    :param new_hobby:
    :return:
    """

    logger.info(
        msg=f"Hobbies: Создание хобби {new_hobby.dict()}", extra=user_config
    )  # noqa

    await HobbyService.create(
        uow=db, token_data=token_data, new_hobby=new_hobby
    )  # noqa


@hobby_router.post(
    path="/add_user_hobby",
    response_model=None,
    status_code=status.HTTP_201_CREATED,
    description="""Добавление нового хобби пользователя""",
    summary="Создание нового хобби пользователя",
)
async def new_user_hobby(
    logger: Annotated[Logger, Depends(logger_dep)],
    db: Annotated[InterfaceUnitOfWork, Depends(UnitOfWork)],  # noqa
    token_data: Annotated[dict, Depends(AuthService.verify)],  # noqa
    id_hobby: int,
    req: Request,
    res: Response,
) -> None:
    """
    Создание нового пользовательского хобби
    :param logger:
    :param db:
    :param token_data:
    :param id_hobby:
    :param req:
    :param res:
    :return:
    """

    logger.info(
        msg=f"Создание пользовательского хобби id_hobby = {id_hobby}",
        extra=user_config,  # noqa
    )  # noqa

    await UserHobbiesService.add_new_hobby(
        token_data=token_data,
        uow=db,
        new_hobby=AddUserHobby(
            id_user=int(token_data.get("sub")), id_hobby=id_hobby
        ),  # noqa
    )


@hobby_router.get(
    path="/user_hobby",
    description="Получение всех пользовательских хобби",
    response_model=UserHobbies,
    status_code=status.HTTP_200_OK,
    summary="Пользовательские хобби",
)
async def my_hobbies(
    logger: Annotated[Logger, Depends(logger_dep)],
    db: Annotated[InterfaceUnitOfWork, Depends(UnitOfWork)],  # noqa
    token_data: Annotated[dict, Depends(AuthService.verify)],  # noqa
    req: Request,
    res: Response,
) -> UserHobbies:
    """
    Пользовательские хобби
    :param logger:
    :param db:
    :param token_data:
    :param req:
    :param res:
    :return:
    """

    return await UserHobbiesService.my_hobbies(token_data=token_data, uow=db)  # noqa


@hobby_router.get(
    path="/all_hobbies",
    response_model=AllHobbies,
    description="Все хобби",
    summary="Все хобби",
    status_code=status.HTTP_200_OK,
)
async def all_hobbies(
    logger: Annotated[Logger, Depends(logger_dep)],
    db: Annotated[InterfaceUnitOfWork, Depends(UnitOfWork)],
    req: Request,
    res: Response,
) -> AllHobbies:
    """
    Все хобби
    :param logger:
    :param db:
    :param req:
    :param res:
    :return:
    """

    logger.info(msg=f"Hobbies: Получение всех хобби", extra=user_config)  # noqa

    return await HobbyService.all_hobby(uow=db)


@hobby_router.delete(
    path="/delete",
    description="""
    Удаление хобби. Доступно только для администратора
    """,
    summary="Удаление хобби",
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_hobby(
    logger: Annotated[Logger, Depends(logger_dep)],
    db: Annotated[InterfaceUnitOfWork, Depends(UnitOfWork)],
    token_data: Annotated[dict, Depends(AuthService.verify)],
    id_hobby: int,
    req: Request,
    res: Response,
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

    logger.info(
        msg="Удаление хобби id = {}".format(id_hobby), extra=user_config
    )  # noqa

    await HobbyService.delete_hobby(
        uow=db, token_data=token_data, id_hobby=id_hobby
    )  # noqa


@hobby_router.delete(
    path="/delete_user_hobby",
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
    description="Удаление пользовательского хобби",
    summary="Удаление хобби пользователя",
)
async def delete_my_hobby(
    logger: Annotated[Logger, Depends(logger_dep)],
    db: Annotated[InterfaceUnitOfWork, Depends(UnitOfWork)],
    token_data: Annotated[dict, Depends(AuthService.verify)],
    id_hobby: int,
    req: Request,
    res: Response,
) -> None:
    """
    Удаление пользовательского хобби
    :param logger:
    :param db:
    :param token_data:
    :param id_hobby:
    :param req:
    :param res:
    :return:
    """

    logger.info(
        msg="Удаление польз. хобби id = {}".format(id_hobby), extra=user_config
    )  # noqa

    await UserHobbiesService.delete_user_hobby(
        token_data=token_data, uow=db, id_hobby=id_hobby
    )
