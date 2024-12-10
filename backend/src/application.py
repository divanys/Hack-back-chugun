from fastapi import FastAPI, APIRouter
from typing import List
from src.core.routers import api_v1_router, auth_router


class EduConnectApplication:
    def __init__(self, lifespan):
        self.__app: FastAPI = FastAPI(title="EduConnect API", lifespan=lifespan)
        self.add_routers(routers=[api_v1_router, auth_router])

    def add_routers(self, routers: List[APIRouter]) -> None:
        """
        Добавление APIRouter's
        :param routers:
        :return:
        """

        for router in routers:
            self.__app.include_router(router=router)

    @property
    def app(self) -> FastAPI:
        return self.__app
