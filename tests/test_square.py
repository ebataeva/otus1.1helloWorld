import pytest

from src.Square import Square


def test_square():
    rect = Square(4)
    assert rect.get_area() == 16


def test_square_zero_width():
    rect = Square(0)
    assert not rect.is_exist()
