from src.Circle import Circle


def test_is_not_exist():
    assert not Circle(-1).is_exist()


def test_is_exist():
    assert Circle(2).is_exist()

def test_area():
    assert Circle(2) == 0
