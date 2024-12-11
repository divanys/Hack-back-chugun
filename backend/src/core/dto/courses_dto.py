from pydantic import BaseModel, Field
from typing import Annotated, List, Any


class CreateCourses(BaseModel):
    title_course: Annotated[str, Field(max_length=255)]
    description_course: Annotated[str, Field()]


class CourseData(CreateCourses):
    hobby: Annotated[Any, Field()]


class AllCourses(BaseModel):
    courses: Annotated[List[CourseData], Field()]


class HobbyCourse(BaseModel):
    id_course: int
    id_hobby: int
