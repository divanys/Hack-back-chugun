from fastapi import HTTPException, status


class AuthErrors:
    @classmethod
    async def no_create_tokens(cls) -> None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Не удалось создать токен"
        )

    @classmethod
    async def no_decode_tokens(cls) -> None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Не удалось декодировать токен"
        )
