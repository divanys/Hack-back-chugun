from datetime import date

from pydantic import BaseModel, EmailStr, Field
from typing import Annotated, List


class RegisterUser(BaseModel):

    email: Annotated[EmailStr, Field()]
    password: Annotated[str, Field(min_length=6)]
    user_name: Annotated[str, Field(max_length=85)]
    user_surname: Annotated[str, Field(max_length=125)]
    phone: Annotated[str, Field()]
    date_birthday: Annotated[date, Field()]
    id_university: int


class AuthUser(BaseModel):
    email: Annotated[EmailStr, Field()]
    password: Annotated[str, Field(min_length=6)]


class AddUserHobby(BaseModel):
    id_hobby: Annotated[int, Field()]
    id_user: Annotated[int, Field()]


class UserHobbies(BaseModel):
    hobbies: Annotated[List[AddUserHobby], Field()]
