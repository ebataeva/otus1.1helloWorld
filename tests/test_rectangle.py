import pytest

from src.Rectangle import Rectangle
from src.Figure import Figure
from src.Triangle import Triangle


def test_rectangle():
    rect = Rectangle(4, 5)
    assert rect.get_area() == 20


def test_rectangle_zero_width():
    rect = Rectangle(0, 5)
    assert not rect.is_exist()


def test_add_figure():
    assert Rectangle(2, 5).get_area() == 10
    assert Rectangle(2, 5).add_area(Triangle(3, 4, 5)) == 16
