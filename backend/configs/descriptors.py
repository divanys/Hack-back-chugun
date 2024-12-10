from typing import Any


class Descriptor:
    def __set_name__(self, owner, name):
        self.__name = "__" + name

    def __get__(self, instance, owner) -> Any:
        return instance.__dict__.get(self.__name)

    def __set__(self, instance, value) -> None:
        if self.__name not in instance.__dict__.keys():
            instance.__dict__[self.__name] = value