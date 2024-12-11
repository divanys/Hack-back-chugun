from pydantic import BaseModel, Field
from typing import Annotated, List


class CreateUniversity(BaseModel):
    name_university: Annotated[str, Field(max_length=125)]


class AllUniversity(BaseModel):
    universities: Annotated[List[CreateUniversity], Field()]
