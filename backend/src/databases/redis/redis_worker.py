import json

from redis.asyncio import Redis
from typing import Any
from configs.database_config import db


class RedisWorker:

    redis = Redis(
        host=db.REDIS_HOST,
        port=db.REDIS_PORT,
        db=0,
    )

    @classmethod
    async def set_key(cls, key, value) -> None:
        """
        Установка данных в redis
        :param key:
        :param value:
        :return:
        """

        await cls.redis.set(name=key, value=value, ex=db.REDIS_LIVE)

    @classmethod
    async def get_value(cls, key) -> Any:
        """
        Получение данных из Redis
        :param key:
        :return:
        """

        data = await cls.redis.get(name=key)
        if data:
            return json.loads(data.decode("utf-8"))
        else:
            return False


async def redis_dep() -> RedisWorker:
    return RedisWorker()
