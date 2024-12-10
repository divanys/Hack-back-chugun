from src.databases import MainBase
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, ForeignKey
from typing import Dict, Union, Any


class Vacancies(MainBase):

    title_description: Mapped[str] = mapped_column(type_=String(100))
    description: Mapped[str] = mapped_column(type_=Text)
    id_user: Mapped[int] = mapped_column(ForeignKey("Users.id"))
    user_data: Mapped["Users"] = relationship(  # noqa
        "Users", back_populates="vacancies", uselist=False  # noqa
    )  # noqa

    def __str__(self) -> str:
        return str(
            {k: v for k, v in self.__dict__.items() if not k.startswith("_")}
        )  # noqa

    def __repr__(self) -> str:
        return self.__str__()

    async def read_model(self) -> Dict[Union[int, str, tuple], Any]:
        return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}  # noqa
