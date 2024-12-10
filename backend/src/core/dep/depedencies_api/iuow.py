from typing import Type
from abc import abstractmethod, ABC
from src.databases.postgres.repositories import (
    UserRepository,
    UserTypesRepository,
)  # noqa


class InterfaceUnitOfWork(ABC):

    user_repository: Type[UserRepository]
    user_type_repository: Type[UserTypesRepository]

    @abstractmethod
    async def __aenter__(self):
        raise NotImplementedError

    @abstractmethod
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        raise NotImplementedError

    @abstractmethod
    async def commit(self):
        raise NotImplementedError