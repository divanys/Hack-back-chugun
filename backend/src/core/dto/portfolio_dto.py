from pydantic import BaseModel, Field
from typing import Annotated, List, Any


class CreatePortfolio(BaseModel):
    id_user: Annotated[int, Field()]
    description: Annotated[str, Field(min_length=1)]


class UserPortfolioInformation(CreatePortfolio):
    my_hobbies: Annotated[List[Any], Field()]
    my_recommends: Annotated[List[Any], Field()]


class HobbiPortfolio(BaseModel):
    id_hobby: int
    id_user: int


class RecommendsPortfolio(BaseModel):
    id_user: int
    id_us_ch: int
    description: str
