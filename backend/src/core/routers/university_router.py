from fastapi import status, APIRouter, Depends
from src.core.dto.university_dto import AllUniversity, CreateUniversity
from src.core.services.university_service import UniversityService
from typing import Annotated
from src.core.dep.depedencies_api import InterfaceUnitOfWork, UnitOfWork
from src.core.dep.auth.auth_service import AuthService
from src.other.logger import logger_dep, user_config
from logging import Logger


university_router: APIRouter = APIRouter(
    prefix="/university", tags=["Universities"]
)  # noqa


@university_router.post(  # noqa
    path="/create_university",
    description="""Создание учебного заведения. Доступно для администратора""",
    summary="Создание учебного заведения",
    response_model=None,
    status_code=status.HTTP_201_CREATED,
)
async def create_vacansy(
    logger: Annotated[Logger, Depends(logger_dep)],
    user_data: Annotated[dict, Depends(AuthService.verify)],
    db: Annotated[InterfaceUnitOfWork, Depends(UnitOfWork)],
    new_univ: CreateUniversity,
) -> None:
    """
    Создание учебного заведения
    :param logger:
    :param user_data:
    :param db:
    :param new_vacansy:
    :return:
    """

    logger.info(msg="University: Создание учебного заведения", extra=user_data)  # noqa

    await UniversityService.create(
        token_data=user_data, uow=db, new_university=new_univ
    )


@university_router.get(
    path="/all_university",
    description="""Все учебные заведения""",
    summary="Получение всех учебных заведений",
    response_model=AllUniversity,
    status_code=status.HTTP_200_OK,
)
async def all_vacancies(
    logger: Annotated[Logger, Depends(logger_dep)],
    db: Annotated[InterfaceUnitOfWork, Depends(UnitOfWork)],
) -> AllUniversity:
    """
    Все учебные заведения
    :param logger:
    :param db:
    :return:
    """

    logger.info(
        msg="University: Получение всех учебных заведений", extra=user_config
    )  # noqa
    return await UniversityService.all_universities(uow=db)  # noqa


@university_router.delete(
    path="/delete",
    description="Удаление учебного заведения. Доступно администратору",
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Удаление учебного заведения",
)
async def delete_university(
    logger: Annotated[Logger, Depends(logger_dep)],
    db: Annotated[InterfaceUnitOfWork, Depends(UnitOfWork)],
    user_data: Annotated[dict, Depends(AuthService.verify)],
    id_univ: int,
) -> None:
    """
    УДаление учебного заведения
    :param logger:
    :param db:
    :param user_data:
    :param id_vancasy:
    :return:
    """

    logger.info(
        msg=f"University: Удаление учебного заведения id = {id_univ}",
        extra=user_data,  # noqa
    )  # noqa

    await UniversityService.delete_university(
        uow=db, token_data=user_data, id_univ=id_univ
    )
