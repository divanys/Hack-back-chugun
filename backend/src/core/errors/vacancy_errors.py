from fastapi.exceptions import HTTPException
from fastapi import status


class VacancyErrors:
    @classmethod
    async def no_create_vacansy(cls) -> None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Не удалось создать вакансию",
        )

    @classmethod
    async def no_delete_vacansy(cls) -> None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Не удалось удалить вакансию",
        )
