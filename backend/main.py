import uvicorn
from src import EduConnectApplication
from fastapi import FastAPI
from configs import api_settings
from src.databases.db_worker import DatabaseWorker
from src.databases.postgres.models import UsersType, Hobbies, University
from sqlalchemy import insert
from src.other.enums.api_enums import UserTypesEnum
from contextlib import asynccontextmanager
from typing import List
import os


@asynccontextmanager
async def lifespan(app: FastAPI) -> None:
    ses = await DatabaseWorker().session
    async with ses.begin() as session:
        try:
            hobbies_list: List[str] = [
                "программирование",
                "python",
                "java",
                "backend",
                "frontend",
                "нейронные сети",
                "математика",
                "аналитика данных",
                "fullstuck",
                "сети и связь",
            ]  # noqa

            for hobby in hobbies_list:
                stmt = insert(Hobbies).values({"text_hobby": hobby})
                await session.execute(stmt)

            await session.commit()
        except Exception:
            pass

    async with ses.begin() as sesstion_f:
        try:
            user_types: dict[int, str] = {
                1: "student",
                2: "worker",
                3: "admin",
                4: "teacher",
            }

            # Создание типов пользователя
            for usertype in [
                UserTypesEnum.USER.value,
                UserTypesEnum.WORK.value,
                UserTypesEnum.ADMIN.value,
                UserTypesEnum.TEACHER.value,
            ]:
                stmt = insert(UsersType).values(
                    name_type=user_types.get(usertype)
                )  # noqa
                await sesstion_f.execute(stmt)

            await sesstion_f.commit()
        except Exception:
            pass

    async with ses.begin() as session_t:
        try:
            universities: List[str] = ["РКСИ", "РГУПС", "ДГТУ", "РИНХ"]
            # Создание типов пользователя
            for univ in universities:
                stmt = insert(University).values(name_university=univ)  # noqa
                await session_t.execute(stmt)
            await session_t.commit()
        except Exception:
            pass

        yield


application: FastAPI = EduConnectApplication(lifespan=lifespan).app


if __name__ == "__main__":
    # Run alembic
    os.system("alembic upgrade head")
    uvicorn.run(
        app=application,
        host=api_settings.API_HOST,
        port=api_settings.API_PORT,
    )
