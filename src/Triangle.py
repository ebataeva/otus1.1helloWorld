from cmath import sqrt

from src.Figure import Figure


class Triangle(Figure):
    def __init__(self, side_1, side_2, side_3) -> None:
        super().__init__()
        self.a = side_1
        self.b = side_2
        self.c = side_3
        self.perimeter = self.a + self.b + self.c

    def add_area(self, figure):
        super().add_area(figure)

    def get_area(self):
        p = self.perimeter / 2
        if self.is_exist():
            self.area = sqrt(p * (p - self.a) * (p - self.b)
                             * (p - self.c))
            return self.area
        else:
            return False

    def is_exist(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return True
        else:
            return False
