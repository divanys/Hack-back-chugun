from src.core.dep.depedencies_api import InterfaceUnitOfWork
from src.core.dto.hobby_dto import CreateHobby, AllHobbies
from src.core.errors.auth_errors import AuthErrors
from src.databases.postgres.models.hobbies import Hobbies
from src.other.enums.api_enums import UserTypesEnum
from src.core.errors.hobby_course_errors import HobbyCoursesErrors


class HobbyService:
    @classmethod
    async def create(
            cls,
            token_data: dict,
            uow: InterfaceUnitOfWork,
            new_hobby: CreateHobby
    ) -> None:
        """
        Создание хобби
        :param token_data:
        :param uow:
        :param new_hobby:
        :return:
        """

        async with uow:
            user_data = await uow.user_repository.get_one(
                _id=token_data.get("sub")
            )  # noqa
            if user_data:
                if user_data[0].id_user_type == UserTypesEnum.TEACHER:
                    is_created = await uow.hobbies_repository.create_data(
                        model_data=Hobbies(
                            text_hobby=new_hobby.text_hobby
                        )
                    )
                    if is_created:
                        return None
                    await HobbyCoursesErrors.no_create_hobby()
            await AuthErrors.no_access()

    @classmethod
    async def all_hobby(cls, uow: InterfaceUnitOfWork) -> AllHobbies:
        """
        Все хобби
        :param uow:
        :return:
        """

        async with uow:
            all_hobby = await uow.hobbies_repository.get_all()
            all_hobbies = AllHobbies(hobbies=[])
            for hobby in all_hobby:
                all_hobbies.hobbies.append(
                    CreateHobby(
                        text_hobby=hobby[0].text_hobby
                    )
                )

            return all_hobbies

    @classmethod
    async def delete_hobby(
            cls,
            uow: InterfaceUnitOfWork,
            token_data: dict,
            id_hobby: int
    ) -> None:
        """
        Удаление хобби
        :param uos:
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
                    is_deleted = await uow.hobbies_repository.delete(_id=id_hobby)
                    if is_deleted:
                        return None
                    await HobbyCoursesErrors.no_delete_hobby()
            await AuthErrors.no_access()
