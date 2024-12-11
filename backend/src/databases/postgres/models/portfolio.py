from src.databases import MainBase
from sqlalchemy.orm import Mapped, mapped_column, relationship  # noqa
from sqlalchemy import ForeignKey, Text
from typing import Dict, Union, Any


class Portfolio(MainBase):
    id_user: Mapped[int] = mapped_column(ForeignKey("Users.id"), unique=True)
    description: Mapped[str] = mapped_column(
        type_=Text, nullable=False, index=False  # noqa
    )  # noqa

    user_data: Mapped["Users"] = relationship(  # noqa
        "Users", back_populates="portfolio_data", uselist=False  # noqa
    )

    def __str__(self) -> str:
        return str(
            {k: v for k, v in self.__dict__.items() if not k.startswith("_")}
        )  # noqa

    def __repr__(self) -> str:
        return self.__str__()

    async def read_model(self) -> Dict[Union[int, str, tuple], Any]:
        return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}  # noqa
