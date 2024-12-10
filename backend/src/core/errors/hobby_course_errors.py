from fastapi import HTTPException, status


class HobbyCoursesErrors:
    @classmethod
    async def no_delete_hobby_courses(cls) -> None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Не удалось удалить хобби курса",
        )
