import bcrypt


class HashService:

    @classmethod
    async def hashed_password(cls, password: str) -> bytes:
        """
        Хэшеирование пароля
        :param password:
        :return:
        """

        return bcrypt.hashpw(
            password=password.encode("utf-8"), salt=bcrypt.gensalt()  # noqa
        )  # noqa

    @classmethod
    async def verify_password(
        cls, password: str, hashed_password: bytes
    ) -> bool:  # noqa
        """
        Проверка пароля
        :param password:
        :param hashed_password:
        :return:
        """

        is_verify = bcrypt.checkpw(  # noqa
            password=password.encode("utf-8"), hashed_password=hashed_password  # noqa
        )

        return is_verify
