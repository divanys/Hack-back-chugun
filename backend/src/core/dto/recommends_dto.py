from pydantic import BaseModel, Field
from typing import Annotated, List


class CreateRecommends(BaseModel):
    id_user: Annotated[int, Field()]
    id_us_ch: Annotated[int, Field()]
    description: Annotated[str, Field()]


class AllUserRecommends(BaseModel):
    recommends: Annotated[List[CreateRecommends], Field()]
    