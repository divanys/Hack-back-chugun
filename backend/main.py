import uvicorn
from backend.src import EduConnectApplication
from fastapi import FastAPI
from backend.configs import api_settings
from src.databases.db_worker import DatabaseWorker
from contextlib import asynccontextmanager

from src.databases.postgres.models import UsersType
from src.other.enums.api_enums import UserTypesEnum
from sqlalchemy import insert
from sqlalchemy import text


@asynccontextmanager
async def lifespan(app: FastAPI) -> None:
    ses = await DatabaseWorker().session
    async with ses.begin() as session:
        try:
            user_types: dict[int, str] = {
                0: "student",
                1: "worker",
                2: "admin",
                3: "teacher"
            }

            for usertype in [UserTypesEnum.USER.value, UserTypesEnum.WORK.value, UserTypesEnum.ADMIN.value,
                             UserTypesEnum.TEACHER.value]:
                stmt = insert(UsersType).values(name_type=user_types.get(usertype)) # noqa
                await session.execute(stmt)

            await session.commit()
            await session.close()
        except Exception as ex:
            pass

        yield


application: FastAPI = EduConnectApplication(lifespan=lifespan).app


if __name__ == "__main__":
    uvicorn.run(
        app=application,
        host=api_settings.API_HOST,
        port=api_settings.API_PORT,
    )
