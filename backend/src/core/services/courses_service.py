from src.databases.postgres.models import Courses, HobbyCourses
from src.databases.postgres.repositories import HobbyCoursesRepository  # noqa
from src.core.dto.courses_dto import (
    AllCourses,
    CourseData,
    CreateCourses,
    HobbyCourse,
)  # noqa
from src.core.dep.depedencies_api import InterfaceUnitOfWork
from src.core.errors.courses_errors import CoursesErrors
from src.other.enums.api_enums import UserTypesEnum


class CoursesService:
    @classmethod
    async def create_course(
        cls,
        uow: InterfaceUnitOfWork,
        token_data: dict,
        new_course: CreateCourses,  # noqa
    ) -> None:
        """
        Создание курса
        :param token_data:
        :param new_course:
        :return:
        """

        async with uow:
            user_data = await uow.user_repository.get_one(
                _id=token_data.get("sub")
            )  # noqa
            if user_data:
                if user_data[0].id_user_type == UserTypesEnum.TEACHER:
                    result = await uow.courses_repository.create_data(
                        model_data=Courses(
                            title_course=new_course.title_course,
                            description_course=new_course.description_course,
                        )
                    )

                    if result:
                        return
                else:
                    await CoursesErrors.no_create_course_with_no_access()
            await CoursesErrors.no_create_course()

    @classmethod
    async def get_all_information(cls, uow: InterfaceUnitOfWork):
        """
        Получение всех курсов
        :param uow:
        :return:
        """

        async with uow:
            courses_data = await uow.courses_repository.get_all()  # noqa
            who_was: list = []
            if courses_data:
                courses = AllCourses(courses=[])
                for course in courses_data:
                    if course[0].title_course in who_was:
                        continue
                    who_was.append(course[0].title_course)
                    courses.courses.append(
                        CourseData(
                            title_course=course[0].title_course,
                            description_course=course[0].description_course,
                            hobby=[
                                await hobby[1].read_model()
                                for hobby in courses_data
                                if hobby[0].title_course
                                == course[0].title_course  # noqa
                                and hobby[1]  # noqa
                            ],  # noqa
                        )
                    )
                return courses
            return AllCourses(courses=[])

    @classmethod
    async def delete_course(
        cls, token_data: dict, uow: InterfaceUnitOfWork, _id: int  # noqa
    ) -> None:
        """
        Удаление курса
        :param token_data:
        :param uow:
        :param _id:
        :return:
        """

        async with uow:
            user_data = await uow.user_repository.get_one(
                _id=token_data.get("sub")
            )  # noqa
            if user_data:
                if user_data[0].id_user_type == UserTypesEnum.TEACHER:
                    is_deleted = await uow.courses_repository.delete(_id=_id)  # noqa
                    if is_deleted:
                        return None

                    await CoursesErrors.no_delete_course()
            await CoursesErrors.no_create_course_with_no_access()

    @classmethod
    async def add_hobby_course(
        cls,
        uow: InterfaceUnitOfWork,
        token_data: dict,
        new_hobby_cs: HobbyCourse,  # noqa
    ):
        """
        Добавление хобби к курсу
        :param uow:
        :param token_data:
        :param id_hobby:
        :return:
        """

        async with uow:
            user_data = await uow.user_repository.get_one(
                _id=token_data.get("sub")
            )  # noqa
            if user_data:
                if user_data[0].id_user_type == UserTypesEnum.TEACHER:
                    add_hobby = await uow.hobby_courses_repository.create_data(
                        model_data=HobbyCourses(
                            id_hobby=new_hobby_cs.id_hobby,
                            id_course=new_hobby_cs.id_course,
                        )
                    )

                    if add_hobby:
                        return None
                await CoursesErrors.no_add_hobby()
            await CoursesErrors.no_create_course_with_no_access()

    @classmethod
    async def delete_hobby(
        cls, uow: InterfaceUnitOfWork, token_data: dict, id_hobby: int  # noqa
    ) -> None:
        """
        Удаление хобби с курса
        :param uow:
        :param token_data:
        :param hobby_id:
        :return:
        """

        async with uow:
            user_data = await uow.user_repository.get_one(
                _id=token_data.get("sub")
            )  # noqa
            if user_data:
                if user_data[0].id_user_type == UserTypesEnum.TEACHER:
                    is_deleted = await uow.hobby_courses_repository.delete(
                        _id=id_hobby
                    )  # noqa
                    if is_deleted:
                        return None
                await CoursesErrors.no_delete_hobby()
            await CoursesErrors.no_create_course_with_no_access()
