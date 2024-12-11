from pydantic import BaseModel, EmailStr, Field
from typing import Annotated, List


class RegisterUser(BaseModel):
    email: Annotated[EmailStr, Field()]
    password: Annotated[str, Field(min_length=6)]


class AuthUser(RegisterUser):
    pass


class AddUserHobby(BaseModel):
    id_hobby: Annotated[int, Field()]
    id_user: Annotated[int, Field()]


class UserHobbies(BaseModel):
    hobbies: Annotated[List[AddUserHobby], Field()]
