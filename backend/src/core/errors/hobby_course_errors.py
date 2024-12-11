from fastapi import HTTPException, status


class HobbyCoursesErrors:
    @classmethod
    async def no_delete_hobby_courses(cls) -> None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Не удалось удалить хобби курса",
        )

    @classmethod
    async def no_delete_hobby(cls) -> None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Не удалось удалить хобби",  # noqa
        )

    @classmethod
    async def no_create_hobby(cls) -> None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Не удалось создать хобби",  # noqa
        )
