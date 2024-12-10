from fastapi import APIRouter
from src.core.routers.user_router import auth_router
from src.core.routers.courses_router import courses_router
from src.core.routers.hobby_router import hobby_router
from typing import List


api_v1_router: APIRouter = APIRouter(prefix="/api/v1", tags=["API-V1"])

api_v1_router.include_router(auth_router)
api_v1_router.include_router(courses_router)
api_v1_router.include_router(hobby_router)


__all__: List[str] = [
    "auth_router",
    "api_v1_router",
    "courses_router",
    "hobby_router",
]  # noqa
