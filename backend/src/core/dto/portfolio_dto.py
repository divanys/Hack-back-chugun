from pydantic import BaseModel, Field
from typing import Annotated, List, Dict


class CreatePortfolio(BaseModel):
    id_user: Annotated[int, Field()]
    description: Annotated[str, Field(min_length=1)]


class UserPortfolioInformation(CreatePortfolio):
    my_hobbies: Annotated[List[Dict], Field()]
    my_recommends: Annotated[List[Dict], Field()]
