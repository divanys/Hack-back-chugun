from typing import Dict, Union, Any

from sqlalchemy import String, Text, Integer, ForeignKey  # noqa
from sqlalchemy.orm import Mapped, mapped_column, relationship  # noqa
from src.databases import MainBase
from typing import List


class University(MainBase):

    name_university: Mapped[str] = mapped_column(
        type_=String(125), nullable=False, unique=True, index=False  # noqa
    )  # noqa

    users: Mapped[List["Users"]] = relationship(  # noqa
        "Users", back_populates="university_data", uselist=True  # noqa
    )

    def __str__(self) -> str:
        return str(
            {k: v for k, v in self.__dict__.items() if not k.startswith("_")}
        )  # noqa

    def __repr__(self):
        return self.__str__()

    async def read_model(self) -> Dict[Union[int, str, tuple], Any]:
        return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}  # noqa
