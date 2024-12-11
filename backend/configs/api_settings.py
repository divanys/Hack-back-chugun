from configs.descriptors import Descriptor
from os import getenv
from dotenv import load_dotenv
from typing import Final


load_dotenv()


class APISettings:
    API_HOST: Final[str] = Descriptor()
    API_PORT: Final[int] = Descriptor()
    TOKEN: Final[str] = Descriptor()
    REFRESH_TOKEN: Final[str] = Descriptor()
    TOKEN_LIFE: Final[int] = Descriptor()
    REFRESH_TOKEN_LIFE: Final[int] = Descriptor()
    ALGORITHM: Final[str] = Descriptor()

    def __init__(self) -> None:
        self.API_HOST = getenv("API_HOST")
        self.API_PORT = int(getenv("API_PORT"))
        self.TOKEN = getenv("TOKEN_SECRET_KEY")
        self.REFRESH_TOKEN = getenv("REFRESH_TOKEN_SECRET_KEY")
        self.TOKEN_LIFE = int(getenv("TOKEN_LIFE"))
        self.REFRESH_TOKEN_LIFE = int(getenv("REFRESH_TOKEN_LIFE"))
        self.ALGORITHM = getenv("ALGORITHM")


api_settings: APISettings = APISettings()
