from src.databases import MainBase
from sqlalchemy.orm import Mapped, mapped_column, relationship  # noqa
from sqlalchemy import String
from typing import List, Dict, Union, Any


class Hobbies(MainBase):
    text_hobby: Mapped[String] = mapped_column(
        type_=String(255), nullable=False, unique=True, index=True  # noqa
    )
    courses: Mapped[List["HobbyCourses"]] = relationship(  # noqa
        "HobbyCourses", back_populates="hobbies", uselist=True  # noqa
    )
    users: Mapped[List["UserHobbies"]] = relationship(  # noqa
        "UserHobbies", back_populates="hobby_data", uselist=True  # noqa
    )

    def __str__(self) -> str:
        return str(
            {k: v for k, v in self.__dict__.items() if not k.startswith("_")}
        )  # noqa

    def __repr__(self) -> str:
        return self.__str__()

    async def read_model(self) -> Dict[Union[int, str, tuple], Any]:
        return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}  # noqa
