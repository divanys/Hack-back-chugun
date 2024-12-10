from abc import abstractmethod, ABC


class CreateInterface(ABC):
    @abstractmethod
    async def create_data(self, *args) -> None:
        raise NotImplementedError
