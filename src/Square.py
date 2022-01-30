
from src.Rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, length, width):
        super().__init__(length, width)
        self.length = length
        self.width = length
        self.area = 0
        self.perimeter = 0


