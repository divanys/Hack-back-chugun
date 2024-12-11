from enum import Enum
from typing import Final


class UserTypesEnum(Enum):
    USER: Final[int] = 1
    ADMIN: Final[int] = 2
    TEACHER: Final[int] = 3
    WORK: Final[int] = 4
