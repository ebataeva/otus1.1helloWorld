from abc import abstractmethod
from typing import Any


class Figure:
    def __init__(self) -> None:
        super().__init__()
        self.area = 0
        self.perimeter = 0

    def add_area(self, figure):
        return self.area + figure.get_area()

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def is_exist(self):
        pass


