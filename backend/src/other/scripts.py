from sqlalchemy.ext.asyncio import AsyncSession
from src.other.enums.api_enums import UserTypesEnum
from sqlalchemy import insert
from src.databases.postgres.models import UsersType, Hobbies
from typing import List


async def create_user_types(session: AsyncSession) -> None:
    """
    Создание пользов. типов
    :param session:
    :return:
    """

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
            stmt = insert(UsersType).values(name_type=user_types.get(usertype))  # noqa
            await session.execute(stmt)

        await session.commit()
    except Exception:
        pass


async def create_hobbies(session: AsyncSession) -> None:
    """
    Создание хобби
    :param session:
    :return:
    """

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
    except Exception as ex:
        print(ex)
        pass
