from pydantic import BaseModel, EmailStr, Field
from typing import Annotated


class RegisterUser(BaseModel):
    email: Annotated[EmailStr, Field()]
    password: Annotated[str, Field(min_length=6)]
