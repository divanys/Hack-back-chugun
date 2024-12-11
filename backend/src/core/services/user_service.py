from starlette.responses import Response

from src.core.dto import RegisterUser, AuthUser
from src.core.dep.depedencies_api import InterfaceUnitOfWork
from src.core.dep.hash.hash_service import HashService
from src.databases.postgres.models import Users
from src.core.errors.user_errors import UserErrors
from src.other.enums.api_enums import UserTypesEnum
from src.core.dep.auth.auth_service import AuthService


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
            hashed_password = await HashService.hashed_password(
                password=user_data.password
            )  # noqa
            is_register = await uow.user_repository.create_data(
                model_data=Users(
                    id_user_type=UserTypesEnum.USER.value,
                    email=user_data.email,
                    hashed_password=hashed_password,
                    user_name=user_data.user_name,
                    user_surname=user_data.user_surname,
                    phone_number=user_data.phone,
                    date_birthday=user_data.date_birthday,
                    id_university=user_data.id_university,
                )  # noqa
            )

            if is_register:
                return None
            await UserErrors.no_register_user()

    @classmethod
    async def login_user(
        cls, uow: InterfaceUnitOfWork, user_data: AuthUser, res: Response
    ) -> None:
        """
        Сервис пользователя - авторизация
        :param uow:
        :param user_data:
        :return:
        """

        async with uow:
            user_data_from_db = await uow.user_repository.find_user_by_email(
                email=user_data.email
            )  # noqa
            print(user_data_from_db)
            if user_data_from_db:
                check_password = await HashService.verify_password(
                    password=user_data.password,
                    hashed_password=user_data_from_db[0].hashed_password,
                )
                if check_password:
                    # Создание токенов
                    access_token: str = await AuthService.create_tokens(
                        user_id=user_data_from_db[0].id, type_token="access"
                    )
                    refresh_token: str = await AuthService.create_tokens(
                        user_id=user_data_from_db[0].id, type_token="refresh"
                    )

                    # Set cookie's
                    res.set_cookie("access_token", access_token)
                    res.set_cookie("refresh_token", refresh_token)
                    return

            await UserErrors.user_not_found()
