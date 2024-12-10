from abc import abstractmethod, ABC


class UpdateInterface(ABC):
    @abstractmethod
    async def update_one(self, _id: int, data: dict) -> None:
        raise NotImplementedError
