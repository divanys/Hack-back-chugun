from dotenv import load_dotenv
from backend.configs.descriptors import Descriptor
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
    REDIS_PORT: Final[str] = Descriptor()

    def __init__(self):
        self.DB_HOST = getenv("DB_NAME")
        self.DB_USER = getenv("DB_USER")
        self.DB_PASSWORD = getenv("DB_PASSWORD")
        self.DB_HOST = getenv("DB_HOST")
        self.DB_PORT = getenv("DB_PORT")
        self.REDIS_HOST = getenv("REDIS_HOST")
        self.REDIS_PORT = getenv("REDIS_PORT")


db: DatabaseConfig = DatabaseConfig()
