from configs.descriptors import Descriptor
from os import getenv
from dotenv import load_dotenv
from typing import Final


load_dotenv()


class APISettings:
    API_HOST: Final[str] = Descriptor()
    API_PORT: Final[int] = Descriptor()

    def __init__(self) -> None:
        self.API_HOST = getenv("API_HOST")
        self.API_PORT = int(getenv("API_PORT"))


api_settings: APISettings = APISettings()
