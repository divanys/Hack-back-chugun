from src.core.dep.depedencies_api import InterfaceUnitOfWork
from src.core.dto.user_dto import AddUserHobby, UserHobbies as UserHobbiesDTO
from src.core.errors.auth_errors import AuthErrors  # noqa
from src.core.errors.user_errors import UserErrors
from src.other.enums.api_enums import UserTypesEnum  # noqa
from src.databases.postgres.models import UserHobbies  # noqa


class UserHobbiesService:

    @classmethod
    async def add_new_hobby(
        cls,
        token_data: dict,
        uow: InterfaceUnitOfWork,
        new_hobby: AddUserHobby,  # noqa
    ) -> None:
        """
        Создание портфолио
        :param token_data:
        :param uow:
        :param new_portfolio:
        :return:
        """

        async with uow:
            user_data = await uow.user_repository.get_one(
                _id=token_data.get("sub")
            )  # noqa
            if user_data:
                is_added = await uow.user_hobbies_repository.create_data(
                    model_data=UserHobbies(
                        id_user=user_data[0].id, id_hobby=new_hobby.id_hobby
                    )
                )

                if is_added:
                    return
                await UserErrors.no_create_user_hobby()

    @classmethod
    async def my_hobbies(
        cls, token_data: dict, uow: InterfaceUnitOfWork
    ) -> UserHobbies:
        """
        Получение всех хобби пользователя
        :param token_data:
        :param uow:
        :return:
        """

        async with uow:
            user_hb = await uow.user_hobbies_repository.get_all(
                _id=int(token_data.get("sub"))
            )
            all_hobbies = UserHobbiesDTO(hobbies=[])
            if user_hb:
                for hobby in user_hb:
                    all_hobbies.hobbies.append(
                        AddUserHobby(
                            id_user=hobby[0].id_user, id_hobby=hobby[0].id_hobby
                        )
                    )
            return all_hobbies

    @classmethod
    async def delete_user_hobby(
        cls,
        token_data: dict,
        id_hobby: int,
        uow: InterfaceUnitOfWork,
    ) -> None:
        """
        Удаление хобби пользователя
        :param token_data:
        :param uow:
        :return:
        """

        async with uow:
            is_deleted = await uow.user_hobbies_repository.delete(
                _id=id_hobby, id_user=int(token_data.get("sub"))
            )  # noqa
            if is_deleted:
                return None
            await UserErrors.no_delete_user_hobby()
