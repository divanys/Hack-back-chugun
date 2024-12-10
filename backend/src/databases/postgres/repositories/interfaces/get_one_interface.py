from abc import abstractmethod, ABC


class GetOneInterface(ABC):
    @abstractmethod
    async def get_one(self, _id: int) -> None:
        raise NotImplementedError
