from src.databases.mongo.collections.forums import ForumsCollection
from src.core.dto.forums_dto import ForumsData
from fastapi import APIRouter, status, Depends
from src.core.dep.auth.auth_service import AuthService
from typing import List, Annotated

from src.other.enums.api_enums import UserTypesEnum

forum_router: APIRouter = APIRouter(
    prefix="/forum",
    tags=["Forum"]
)


@forum_router.post(
    path="/create",
    description="Создание форума",
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT
)
async def create_forums(
        title: str,
        tags: List[str],
        text_question: str,
        user_data: Annotated[dict, Depends(AuthService.verify)]
) -> None:

    await ForumsCollection().create_forum(
        id_user=int(user_data.get("sub")),
        title=title,
        tags=tags,
        text_question=text_question
    )


@forum_router.get(
    path="/get_all_forums",
    response_model=List[ForumsData],
    description="Все форумы",
    status_code=status.HTTP_200_OK
)
async def get_all_forums():
    res = await ForumsCollection().get_all_forums()
    print(res)
    return res
