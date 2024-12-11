from fastapi import HTTPException, status


class UserErrors:
    @classmethod
    async def no_register_user(cls) -> None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Не удалось зарегистрировать пользователя",
        )

    @classmethod
    async def user_not_found(cls) -> None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Пользователь не был найден",  # noqa
        )

    @classmethod
    async def no_delete_user_hobby(cls) -> None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Не удалось удалить хобби пользователя",
        )

    @classmethod
    async def no_create_user_hobby(cls) -> None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Не удалось добавить новое хобби пользователю",
        )
