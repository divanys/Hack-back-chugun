from src.core.dto import RegisterUser
from src.core.dep.depedencies_api import InterfaceUnitOfWork
from src.core.dep.hash.hash_service import HashService
from src.databases.postgres.models import Users
from src.core.errors.user_errors import UserErrors
from src.other.enums.api_enums import UserTypesEnum


class UserService:

    @classmethod
    async def register_user_on_db(
        cls, user_data: RegisterUser, uow: InterfaceUnitOfWork
    ) -> None:
        """
        Сервис пользователя - регистрация
        :param engine:
        :param user_data:
        :return:
        """

        async with uow:
            hashed_password = HashService.hashed_password(
                password=user_data.password
            )  # noqa
            is_register = await uow.user_repository.create_data(
                model_data=Users(
                    id_user_type=UserTypesEnum.USER.value,
                    email=user_data.email,
                    hashed_password=hashed_password,
                )  # noqa
            )

            if is_register:
                return None
            await UserErrors.no_register_user()
