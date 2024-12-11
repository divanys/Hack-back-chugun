import uvicorn
from src import EduConnectApplication
from fastapi import FastAPI
from configs import api_settings
from src.databases.db_worker import DatabaseWorker
from contextlib import asynccontextmanager
import os
from src.other.scripts import create_hobbies, create_user_types


@asynccontextmanager
async def lifespan(app: FastAPI) -> None:
    ses = await DatabaseWorker().session
    async with ses.begin() as session:
        await create_hobbies(session=session)
        await create_user_types(session=session)
        await session.close()
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
