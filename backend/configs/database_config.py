from dotenv import load_dotenv
from configs.descriptors import Descriptor
from os import getenv
from typing import Final


load_dotenv()


class DatabaseConfig:

    DB_NAME: Final[str] = Descriptor()
    DB_USER: Final[str] = Descriptor()
    DB_PASSWORD: Final[str] = Descriptor()
    DB_HOST: Final[str] = Descriptor()
    DB_PORT: Final[str] = Descriptor()
    REDIS_HOST: Final[str] = Descriptor()
    REDIS_PORT: Final[int] = Descriptor()
    REDIS_LIVE: Final[int] = Descriptor()
    MONGO_URI: Final[str] = Descriptor()

    def __init__(self):
        self.DB_HOST = getenv("DB_HOST")
        self.DB_USER = getenv("DB_USER")
        self.DB_PASSWORD = getenv("DB_PASSWORD")
        self.DB_NAME = getenv("DB_NAME")
        self.DB_PORT = getenv("DB_PORT")
        self.REDIS_HOST = getenv("REDIS_HOST")
        self.REDIS_PORT = int(getenv("REDIS_PORT"))
        self.REDIS_LIVE = int(getenv("REDIS_LIVE"))
        self.MONGO_URI = getenv("MONGO_URI")


db: DatabaseConfig = DatabaseConfig()
