from src.databases import MainBase
from sqlalchemy.orm import Mapped, mapped_column, relationship  # noqa
from sqlalchemy import ForeignKey
from typing import Dict, Union, Any


class HobbyCourses(MainBase):
    id_course: Mapped[int] = mapped_column(ForeignKey("Courses.id"))
    id_hobby: Mapped[int] = mapped_column(ForeignKey("Hobbies.id"))
    course_data: Mapped["Courses"] = relationship(  # noqa
        "Courses", back_populates="hobbies", uselist=False  # noqa
    )
    hobbies: Mapped["Hobby"] = relationship(  # noqa
        "Hobbies", back_populates="courses", uselist=False  # noqa
    )

    def __str__(self) -> str:
        return str(
            {k: v for k, v in self.__dict__.items() if not k.startswith("_")}
        )  # noqa

    def __repr__(self) -> str:
        return self.__str__()

    async def read_model(self) -> Dict[Union[int, str, tuple], Any]:
        return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}  # noqa
