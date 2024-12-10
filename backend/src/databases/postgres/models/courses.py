from src.databases import MainBase
from sqlalchemy.orm import Mapped, mapped_column, relationship  # noqa
from sqlalchemy import String
from typing import List, Dict, Union, Any

from src.databases.postgres.models.tasks import Tasks


class Courses(MainBase):

    title_course: Mapped[String] = mapped_column(
        type_=String(255), nullable=False, unique=True, index=True  # noqa
    )

    hobbies: Mapped[List["HobbyCourses"]] = relationship(  # noqa
        "HobbyCourses", back_populates="course_data", uselist=True  # noqa
    )
    tasks_data: Mapped[List["Tasks"]] = relationship(
        "Tasks", back_populates="course_data", uselist=True  # noqa
    )

    def __str__(self) -> str:
        return str(
            {k: v for k, v in self.__dict__.items() if not k.startswith("_")}
        )  # noqa

    def __repr__(self) -> str:
        return self.__str__()

    async def read_model(self) -> Dict[Union[int, str, tuple], Any]:
        return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}  # noqa
