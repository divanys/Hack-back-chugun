from fastapi import status, APIRouter, Depends
from src.core.dto.vacancies_dto import CreateVacancies, AllVacancies
from src.core.services.vacancies_service import VacanciesService
from typing import Annotated
from src.core.dep.depedencies_api import InterfaceUnitOfWork, UnitOfWork
from src.core.dep.auth.auth_service import AuthService
from src.other.logger import logger_dep, user_config
from src.databases.redis.redis_worker import RedisWorker, redis_dep
from logging import Logger


vacansy_router: APIRouter = APIRouter(prefix="/vacansy", tags=["Vacancies"])


@vacansy_router.post(
    path="/create_vacansy",
    description="""Создание вакансии. Доступно для работодателей""",
    summary="Создание вакансии",
    response_model=None,
    status_code=status.HTTP_201_CREATED,
)
async def create_vacansy(
    logger: Annotated[Logger, Depends(logger_dep)],
    user_data: Annotated[dict, Depends(AuthService.verify)],
    db: Annotated[InterfaceUnitOfWork, Depends(UnitOfWork)],
    new_vacansy: CreateVacancies,
) -> None:
    """
    Создание вакансии
    :param logger:
    :param user_data:
    :param db:
    :param new_vacansy:
    :return:
    """

    logger.info(
        msg=f"Vacansy: Создание вакансии {new_vacansy.dict()}", extra=user_data
    )  # noqa

    await VacanciesService.create(  # noqa
        token_data=user_data, uow=db, new_vacansy=new_vacansy
    )


@vacansy_router.get(
    path="/all_vacansy",
    description="""Все вакансии""",
    summary="Получение всех вакансий",
    response_model=AllVacancies,
    status_code=status.HTTP_200_OK,
)
async def all_vacancies(
    logger: Annotated[Logger, Depends(logger_dep)],
    redis: Annotated[RedisWorker, Depends(redis_dep)],
    db: Annotated[InterfaceUnitOfWork, Depends(UnitOfWork)],
) -> AllVacancies:
    """
    Все вакансии
    :param logger:
    :param db:
    :return:
    """

    logger.info(msg=f"Vacansy: Получение всех вакансий", extra=user_config)  # noqa

    redis_data = await redis.get_value(key="all_vacansy")
    if redis_data:
        return redis_data
    else:
        all_vac = await VacanciesService.all_vacansy(uow=db)  # noqa
        await redis.set_key(key="all_vacansy", value=all_vac.json())
        return all_vac


@vacansy_router.delete(
    path="/delete",
    description="Удаление вакансии. Доступно администратору",
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Удаление вакансии",
)
async def delete_vacansy(
    logger: Annotated[Logger, Depends(logger_dep)],
    db: Annotated[InterfaceUnitOfWork, Depends(UnitOfWork)],
    user_data: Annotated[dict, Depends(AuthService.verify)],
    id_vancasy: int,
) -> None:
    """
    УДаление вакансии
    :param logger:
    :param db:
    :param user_data:
    :param id_vancasy:
    :return:
    """

    logger.info(
        msg=f"Vacansy: Удаление вакансии id={id_vancasy}", extra=user_data
    )  # noqa

    await VacanciesService.delete_vacansy(  # noqa
        uow=db, token_data=user_data, id_vac=id_vancasy
    )
