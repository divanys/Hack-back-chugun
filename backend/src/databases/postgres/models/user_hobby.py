from src.databases import MainBase
from sqlalchemy.orm import Mapped, mapped_column, relationship  # noqa
from sqlalchemy import ForeignKey
from typing import Dict, Union, Any

from src.databases.postgres.models.hobbies import Hobbies  # noqa


class UserHobbies(MainBase):
    id_user: Mapped[int] = mapped_column(ForeignKey("Users.id"))  # noqa
    id_hobby: Mapped[int] = mapped_column(ForeignKey("Hobbies.id"))  # noqa
    user_data: Mapped["Courses"] = relationship(  # noqa
        "Users", back_populates="hobbies", uselist=False  # noqa
    )
    hobby_data: Mapped["Hobbies"] = relationship(
        "Hobbies", back_populates="users", uselist=False  # noqa
    )

    def __str__(self) -> str:
        return str(
            {k: v for k, v in self.__dict__.items() if not k.startswith("_")}
        )  # noqa

    def __repr__(self) -> str:
        return self.__str__()

    async def read_model(self) -> Dict[Union[int, str, tuple], Any]:
        return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}  # noqa
