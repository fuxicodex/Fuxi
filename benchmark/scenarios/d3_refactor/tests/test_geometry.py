import math
import pytest
from src.geometry import (
    calc_area_of_rectangle,
    calc_perimeter_of_rectangle,
    calc_area_of_circle,
    calc_circumference_of_circle,
    classify_triangle,
)


def test_rectangle_area():
    assert calc_area_of_rectangle(3, 4) == 12


def test_rectangle_perimeter():
    assert calc_perimeter_of_rectangle(3, 4) == 14


def test_circle_area():
    assert calc_area_of_circle(1) == pytest.approx(math.pi)


def test_circle_circumference():
    assert calc_circumference_of_circle(1) == pytest.approx(2 * math.pi)


def test_classify_triangle():
    assert classify_triangle(2, 2, 2) == "equilateral"
    assert classify_triangle(2, 2, 3) == "isosceles"
    assert classify_triangle(3, 4, 5) == "scalene"
    assert classify_triangle(1, 2, 3) == "not a triangle"
    assert classify_triangle(0, 4, 5) == "not a triangle"
