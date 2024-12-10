from src.databases import MainBase
from sqlalchemy.orm import Mapped, mapped_column, relationship  # noqa
from sqlalchemy import Text, ForeignKey
from typing import Dict, Union, Any


class Recommends(MainBase):

    # Студент
    id_user: Mapped[int] = mapped_column(ForeignKey("Users.id"))

    # Оценщик
    id_us_ch: Mapped[int] = mapped_column(ForeignKey("Users.id"))

    description: Mapped[str] = mapped_column(type_=Text)

    student_data: Mapped["Users"] = relationship(  # noqa
        "Users", back_populates="rec_student_data", uselist=False, foreign_keys=[id_user]  # noqa
    )

    us_ch_data: Mapped["Users"] = relationship(  # noqa
        "Users", back_populates="rec_us_ch_data", uselist=False, foreign_keys=[id_us_ch]  # noqa
    )

    def __str__(self) -> str:
        return str(
            {k: v for k, v in self.__dict__.items() if not k.startswith("_")}
        )  # noqa

    def __repr__(self) -> str:
        return self.__str__()

    async def read_model(self) -> Dict[Union[int, str, tuple], Any]:
        return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}  # noqa
