
from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def is_exist(self):
        if type(self.width) != str and type(self.length) != str:
            if self.width > 0 and self.length > 0:
                return True
            else:
                return False
        return False

    def get_area(self):
        if self.is_exist():
            self.area = self.length * self.width
            return self.area
        else:
            return False

