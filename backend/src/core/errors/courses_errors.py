from fastapi import HTTPException, status


class CoursesErrors:
    @classmethod
    async def no_delete_course(cls) -> None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Не удалось удалить курс",  # noqa
        )

    @classmethod
    async def no_create_course(cls) -> None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Не удалось создать курс",  # noqa
        )

    @classmethod
    async def no_create_course_with_no_access(cls) -> None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Не удалось создать курс, недостаточно прав",  # noqa
        )

    @classmethod
    async def no_add_hobby(cls) -> None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Не удалось добавить хобби к курсу",  # noqa
        )

    @classmethod
    async def no_delete_hobby(cls) -> None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Не удалось удалить хобби с курса",  # noqa
        )
