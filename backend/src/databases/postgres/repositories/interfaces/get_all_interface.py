from abc import abstractmethod, ABC


class GetAllInterface(ABC):
    @abstractmethod
    async def get_all(self, _id: int) -> None:
        raise NotImplementedError
