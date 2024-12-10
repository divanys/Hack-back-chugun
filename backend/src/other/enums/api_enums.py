from enum import Enum
from typing import Final


class UserTypesEnum(Enum):
    USER: Final[int] = 0
    ADMIN: Final[int] = 1
    TEACHER: Final[int] = 2
    WORK: Final[int] = 3
