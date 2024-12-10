from typing import List
from src.databases.postgres.repositories.general_repositories import (
    GeneralRepository,
)  # noqa
from src.databases.postgres.repositories.user_repository import UserRepository  # noqa
from src.databases.postgres.repositories.user_type_repository import (
    UserTypesRepository,
)  # noqa

__all__: List[str] = [
    "GeneralRepository",
    "UserRepository",
    "UserTypesRepository",
]  # noqa
