from src.Square import Square
from src.Triangle import Triangle

def test_square():
    triangle = Triangle(4, 3, 5)
    assert triangle.get_area() == 6


def test_triangle_zero_width():
    triangle  = Triangle(0, 3, 5)
    assert not triangle.is_exist()


def test_add_figure():
    assert Triangle(3, 4, 5).add_area(Square(1))==7
