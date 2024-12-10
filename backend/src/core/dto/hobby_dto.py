from pydantic import BaseModel, Field
from typing import Annotated, List


class CreateHobby(BaseModel):
    text_hobby: Annotated[str, Field(max_length=255)]


class AllHobbies(BaseModel):
    hobbies: Annotated[List[CreateHobby], Field()]
