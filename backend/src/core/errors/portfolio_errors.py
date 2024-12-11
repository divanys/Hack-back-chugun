from fastapi import HTTPException, status


class PortfolioErrors:
    @classmethod
    async def no_create_portfolio(cls) -> None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Не удалось создать портфолио",  # noqa
        )

    @classmethod
    async def no_delete_portfolio(cls) -> None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Не удалось удалить портфолио",  # noqa
        )

    @classmethod
    async def no_found_portfolio(cls) -> None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Не удалось найти портфолио",  # noqa
        )
