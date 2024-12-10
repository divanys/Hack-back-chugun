from typing import Dict, Union, Any

from sqlalchemy import String, Text, Integer, ForeignKey  # noqa
from sqlalchemy.dialects.postgresql import BYTEA
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.databases import MainBase
from typing import List

from src.databases.postgres.models.portfolio import Portfolio
from src.databases.postgres.models.recommends import Recommends
from src.databases.postgres.models.university import University


class Users(MainBase):

    email: Mapped[str] = mapped_column(
        type_=String(150), nullable=False, unique=True, index=True  # noqa
    )  # noqa
    hashed_password: Mapped[str] = mapped_column(
        type_=BYTEA, nullable=False, unique=False, index=False  # noqa
    )  # noqa
    user_name: Mapped[str] = mapped_column(
        type_=String(85), nullable=True, unique=False, index=False  # noqa
    )  # noqa
    avatar_url: Mapped[str] = mapped_column(
        type_=Text, nullable=True, unique=False, index=False  # noqa
    )
    phone_number: Mapped[str] = mapped_column(
        type_=String(25), nullable=True, unique=False, index=True  # noqa
    )

    id_user_type: Mapped[int] = mapped_column(ForeignKey("Userstype.id"))
    id_university: Mapped[int] = mapped_column(ForeignKey("University.id"), nullable=True)

    university_data: Mapped["University"] = relationship(
        "University", back_populates="users", uselist=False  # noqa
    )

    rec_student_data: Mapped[List["Recommends"]] = relationship(
        "Recommends", back_populates="student_data", uselist=True, foreign_keys=[Recommends.id_user]  # noqa
    )

    rec_us_ch_data: Mapped[List["Recommends"]] = relationship(
        "Recommends", back_populates="us_ch_data", uselist=True, foreign_keys=[Recommends.id_us_ch]  # noqa
    )

    portfolio_data: Mapped["Portfolio"] = relationship(
        "Portfolio", back_populates="user_data", uselist=False  # noqa
    )

    types: Mapped["UsersType"] = relationship(
        "UsersType", back_populates="users", uselist=False
    )

    hobbies: Mapped[List["UserHobbies"]] = relationship(
        "UserHobbies", back_populates="user_data", uselist=True
    )

    vacancies: Mapped[List["Vacancies"]] = relationship( # noqa
        "Vacancies", back_populates="user_data", uselist=True
    ) # noqa

    def __str__(self) -> str:
        return str(
            {k: v for k, v in self.__dict__.items() if not k.startswith("_")}
        )  # noqa

    def __repr__(self):
        return self.__str__()  # noqa

    async def read_model(self) -> Dict[Union[int, str, tuple], Any]:
        return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}  # noqa
