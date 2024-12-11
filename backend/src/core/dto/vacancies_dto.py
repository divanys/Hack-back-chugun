from pydantic import BaseModel, Field
from typing import Annotated, List


class CreateVacancies(BaseModel):
    title_description: Annotated[str, Field(max_length=100)]
    description: Annotated[str, Field()]
    id_user: Annotated[int, Field()]


class AllVacancies(BaseModel):
    vacancies: Annotated[List[CreateVacancies], Field()]
