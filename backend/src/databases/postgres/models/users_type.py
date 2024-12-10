from src.databases import MainBase
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from typing import Dict, Union, Any


class UsersType(MainBase):

    name_type: Mapped[str] = mapped_column(type_=String(100))
    users: Mapped[List["Users"]] = relationship(  # noqa
        "Users", back_populates="types", uselist=True
    )  # noqa

    def __str__(self) -> str:
        return str(
            {k: v for k, v in self.__dict__.items() if not k.startswith("_")}
        )  # noqa

    def __repr__(self) -> str:
        return self.__str__()

    async def read_model(self) -> Dict[Union[int, str, tuple], Any]:
        return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}  # noqa
