from typing import Dict, Union, Any
import json
from sqlalchemy import String, Text, Integer, ForeignKey, JSON  # noqa
from sqlalchemy.orm import Mapped, mapped_column, relationship  # noqa
from src.databases import MainBase


class Tasks(MainBase):

    text_task: Mapped[str] = mapped_column(
        type_=String(255), nullable=False, unique=False, index=True  # noqa
    )
    task_literal: Mapped[json] = mapped_column(
        type_=JSON(), nullable=True, unique=False, index=False  # noqa
    )
    id_course: Mapped[int] = mapped_column(ForeignKey("Courses.id"))  # noqa

    course_data: Mapped["Courses"] = relationship(  # noqa
        "Courses", back_populates="tasks_data", uselist=False  # noqa
    )

    def __str__(self) -> str:
        return str(
            {k: v for k, v in self.__dict__.items() if not k.startswith("_")}
        )  # noqa

    def __repr__(self):
        return self.__str__()

    async def read_model(self) -> Dict[Union[int, str, tuple], Any]:
        return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}  # noqa
