from typing import List
from src.databases.postgres.repositories.interfaces.update_interface import (
    UpdateInterface,
)
from src.databases.postgres.repositories.interfaces.create_interface import (
    CreateInterface,
)
from src.databases.postgres.repositories.interfaces.get_one_interface import (
    GetOneInterface,
)
from src.databases.postgres.repositories.interfaces.get_all_interface import (
    GetAllInterface,
)
from src.databases.postgres.repositories.interfaces.delete_interface import (
    DeleteInterface,
)


__all__: List[str] = [
    "DeleteInterface",
    "UpdateInterface",
    "CreateInterface",
    "GetAllInterface",
    "GetOneInterface",
]
