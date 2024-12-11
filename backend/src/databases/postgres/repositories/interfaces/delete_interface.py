from abc import abstractmethod, ABC


class DeleteInterface(ABC):
    @abstractmethod
    async def delete(self, _id: int, *args) -> None:
        raise NotImplementedError
