from fastapi import HTTPException, status


class RecommendsErrors:
    @classmethod
    async def no_create_recommends(cls) -> None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Не удалось создать рекомендацию"
        )

    @classmethod
    async def no_delete_recommends(cls) -> None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Не удалось удалить рекомендацию"
        )
