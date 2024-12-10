import jwt
from typing import Literal

from starlette.responses import Response

from configs import api_settings
from datetime import timedelta, datetime
from typing import Any
from src.core.errors.auth_errors import AuthErrors
from fastapi import Request


class AuthService:
    @classmethod
    async def create_tokens(cls, user_id: int, type_token: Literal["access", "refresh"]) -> str:
        """
        Создание токена
        :param user_id:
        :return:
        """

        try:
            match type_token:
                case "access":
                    data: dict[str, Any] = {"sub": user_id}
                    data.update({"exp": (datetime.utcnow() + timedelta(minutes=api_settings.TOKEN_LIFE))}) # noqa
                    token = jwt.encode(data, key=api_settings.TOKEN, algorithm=api_settings.ALGORITHM) # noqa
                    return token
                case "refresh":
                    data: dict[str, Any] = {"sub": user_id}
                    data.update({"exp": (datetime.utcnow() + timedelta(days=api_settings.TOKEN_LIFE))}) # noqa
                    token = jwt.encode(data, key=api_settings.REFRESH_TOKEN, algorithm=api_settings.ALGORITHM) # noqa
                    return token
                case _:
                    await AuthErrors.no_create_tokens()
        except Exception:
            await AuthErrors.no_create_tokens()

    @classmethod
    async def decode_token(cls, type_token: Literal["access", "refresh"], token: str) -> dict: # noqa
        """
        Декодирование токена
        :param type_token:
        :param token:
        :return:
        """

        try:
            match type_token:
                case "access":
                    token_data = jwt.decode(token, key=api_settings.TOKEN, algorithms=[api_settings.ALGORITHM])  # noqa
                    return token_data
                case "refresh":
                    token_data = jwt.decode(token, key=api_settings.REFRESH_TOKEN, algorithms=[api_settings.ALGORITHM])  # noqa
                    return token_data
                case _:
                    await AuthErrors.no_decode_tokens()
        except Exception:
            await AuthErrors.no_create_tokens()

    @classmethod
    async def verify(cls, type_token: Literal["access", "refresh"], req: Request, res: Response) -> str: # noqa
        """
        Проверка токена
        :param type_token:
        :param token:
        :return:
        """

        cookies = req.cookies

        try:
            token_data = jwt.decode(cookies.get("access_token"), key=api_settings.TOKEN, algorithms=[api_settings.ALGORITHM])  # noqa
            if token_data:
                return token_data
            else:
                refresh_token_data: dict = await cls.decode_token(type_token="refresh", token=cookies.get("refresh_token"))
                if refresh_token_data:
                    new_access_token = await cls.create_tokens(user_id=refresh_token_data.get("sub"), type_token="access") # noqa
                    res.set_cookie("access_token", new_access_token)
                    return new_access_token
        except Exception:
            await AuthErrors.no_create_tokens()
