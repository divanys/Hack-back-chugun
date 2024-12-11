from typing import List, Annotated, Dict
from pydantic import BaseModel, Field


class CreateForum(BaseModel):
    pass


class ForumsData(BaseModel):

    title: Annotated[str, Field()]
    tags: Annotated[List[str], Field()]
    text_question: Annotated[str, Field()]
    comments: Annotated[List[Dict], Field()]
