from fastapi import HTTPException, status


class UniversityErrors:

    @classmethod
    async def no_create_university(cls) -> None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Не удалось создать учебное заведение",
        )

    @classmethod
    async def no_delete_university(cls) -> None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Не удалось удалить учебное заведение",
        )
