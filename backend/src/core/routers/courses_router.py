from logging import Logger

from fastapi import APIRouter, Depends, status
from fastapi.responses import Response
from fastapi.requests import Request

from src.core.dep.auth.auth_service import AuthService
from src.core.dep.depedencies_api import InterfaceUnitOfWork, UnitOfWork  # noqa
from typing import Annotated

from src.core.services.courses_service import CoursesService
from src.databases.redis.redis_worker import RedisWorker
from src.other import logger_dep, user_config
from src.core.dto.courses_dto import CreateCourses, AllCourses, HobbyCourse  # noqa
from src.databases.redis.redis_worker import redis_dep

courses_router: APIRouter = APIRouter(prefix="/courses", tags=["Courses"])


@courses_router.post(
    path="/create",
    description="""
    Courses: Создание курса
    Доступен для преподавателя
    """,
    summary="Создание курса",
    response_model=None,
    status_code=status.HTTP_201_CREATED,
)
async def create_course(
    db: Annotated[InterfaceUnitOfWork, Depends(UnitOfWork)],
    logger: Annotated[Logger, Depends(logger_dep)],
    token_data: Annotated[dict, Depends(AuthService.verify)],
    new_course_data: CreateCourses,
    req: Request,
    res: Response,
) -> None:
    """
    Создание курса
    :param db:
    :param logger:
    :param token_data:
    :param new_course_data:
    :param req:
    :param res:
    :return:
    """

    logger.info(
        msg=f"Courses: Создание курса = {new_course_data}", extra=user_config
    )  # noqa

    await CoursesService.create_course(
        uow=db, token_data=token_data, new_course=new_course_data
    )


@courses_router.post(
    path="/add_hobby",
    description="""
    Добавление хобби к курсу
    """,
    summary="Добавление хобби",
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
)
async def add_hobby_in_course(
    logger: Annotated[Logger, Depends(logger_dep)],
    db: Annotated[InterfaceUnitOfWork, Depends(UnitOfWork)],
    user_data: Annotated[dict, Depends(AuthService.verify)],
    new_hobby: HobbyCourse,
) -> None:
    """
    Добавление хобби к курсу
    :param logger:
    :param db:
    :param user_data:
    :param new_hobby:
    :return:
    """

    logger.info(
        msg=f"Courses: Добавление хобби = {new_hobby}", extra=user_config
    )  # noqa

    await CoursesService.add_hobby_course(
        uow=db, token_data=user_data, new_hobby_cs=new_hobby
    )


@courses_router.get(
    path="/all_courses",
    description="""
    Получение информации о всех курсах
    """,
    summary="Все курсы",
    response_model=AllCourses,
    status_code=status.HTTP_200_OK,
)
async def all_courses(
    logger: Annotated[Logger, Depends(logger_dep)],
    db: Annotated[InterfaceUnitOfWork, Depends(UnitOfWork)],
    redis: Annotated[RedisWorker, Depends(redis_dep)],
) -> AllCourses:
    """
    Получение всех курсов
    :param logger:
    :param token_data:
    :param db:
    :return:
    """

    logger.info(msg=f"Courses: Получение всех курсов", extra=user_config)  # noqa

    redis_data = await redis.get_value(key="all_courses")
    if redis_data:
        return redis_data
    else:
        courses = await CoursesService.get_all_information(uow=db)
        await redis.set_key(key="all_courses", value=courses.json())
        return courses


@courses_router.delete(
    path="/delete",
    description="""
    Удаление курса
    """,
    summary="Удаление курса",
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_course(
    logger: Annotated[Logger, Depends(logger_dep)],
    db: Annotated[InterfaceUnitOfWork, Depends(UnitOfWork)],
    token_data: Annotated[dict, Depends(AuthService.verify)],
    id_course: int,
) -> None:
    """
    Удаление курса
    :param logger:
    :param db:
    :param token_data:
    :param id_course:
    :return:
    """

    logger.info(msg=f"Courses: Удаление курса = {id_course}", extra=user_config)  # noqa

    await CoursesService.delete_course(
        token_data=token_data, uow=db, _id=id_course
    )  # noqa


@courses_router.delete(
    path="/delete_hobby",
    response_model=None,
    description="Удаление хобби",
    summary="Удаление хобби",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_hobby(
    logger: Annotated[Logger, Depends(logger_dep)],
    db: Annotated[InterfaceUnitOfWork, Depends(UnitOfWork)],
    token_data: Annotated[dict, Depends(AuthService.verify)],
    id_hobby: int,
) -> None:
    """
    Удаление хобби с курса
    :param logger:
    :param db:
    :param token_data:
    :param id_hobby:
    :return:
    """

    logger.info(
        msg=f"Courses: Удаление хобби с курса = {id_hobby}", extra=user_config
    )  # noqa

    await CoursesService.delete_hobby(
        uow=db, token_data=token_data, id_hobby=id_hobby
    )  # noqa
