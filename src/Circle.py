from abc import ABC

from src.Figure import Figure
import math


class Circle(Figure, ABC):

    def __init__(self, r) -> None:
        self.r = r
        super().__init__()

    def get_area(self):
        return int(math.pi * self.r ** 2)

    def is_exist(self):
        if self.r > 0:
            return True
        else:
            return False
