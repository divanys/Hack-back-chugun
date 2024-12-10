from fastapi import FastAPI, APIRouter
from typing import List


class EduConnectApplication:
    def __init__(self):
        self.__app: FastAPI = FastAPI(title="EduConnect API")

    async def add_routers(self, routers: List[APIRouter]) -> None:
        """
        Добавление APIRouter's
        :param routers:
        :return:
        """

        for router in routers:
            self.app.include_router(router)

    @property
    def app(self) -> FastAPI:
        return self.__app
