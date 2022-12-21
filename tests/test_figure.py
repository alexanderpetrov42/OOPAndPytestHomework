from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle
import pytest as pytest


@pytest.fixture()
def circle_addarea():
    circle = Circle("Circle", 6)
    triangle = Triangle("Triangle", 13, 14, 15)
    return circle.add_area(triangle)


def test_assert_circle_addarea(circle_addarea):
    assert circle_addarea == 197.04


@pytest.fixture()
def rectangle_area():
    rectangle = Rectangle("Rectangle", 5, 6)
    return rectangle.area()


def test_assert_rectangle_area_value(rectangle_area):
    assert rectangle_area == 30


@pytest.fixture()
def triangle_addarea():
    square = Square("Square", 6)
    triangle = Triangle("Triangle", 13, 14, 15)
    return triangle.add_area(square)


def test_assert_addarea_value(triangle_addarea):
    assert triangle_addarea == 120.0


@pytest.fixture()
def triangle_area():
    triangle = Triangle("Triangle", 13, 14, 15)
    return triangle.area()


def test_assert_triangle_area_value(triangle_area):
    assert triangle_area == 84.0


@pytest.fixture()
def square_area():
    square = Square("Square", 6)
    return square.area()


def test_assert_square_area_value(square_area):
    assert square_area == 36


@pytest.fixture()
def wrong_triangle():
    pass


def test_assert_wrong_triangle():
    with pytest.raises(ValueError):
        Triangle("Triangle", 13, 14, 0)


class Wrong:
    pass


@pytest.fixture()
def wrong_figure():
    circle = Circle("Circle", 6)
    wrong_figure = Wrong()
    return circle.add_area(wrong_figure)


def test_assert_wrong_figure_addarea(wrong_figure):
    assert wrong_figure.__name__ == 'ValueError'
