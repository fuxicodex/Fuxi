"""Geometry helpers for rectangles, circles and triangles.

Public behavior is identical to the original module; only the internals were
cleaned up: the pi literal became a named constant, parameters got descriptive
names, and the triangle rules were split into small predicates.
"""

import math

PI = math.pi
TAU = 2 * math.pi

EQUILATERAL = "equilateral"
ISOSCELES = "isosceles"
SCALENE = "scalene"
NOT_A_TRIANGLE = "not a triangle"


def calc_area_of_rectangle(width, height):
    """Area of a rectangle."""
    return width * height


def calc_perimeter_of_rectangle(width, height):
    """Perimeter of a rectangle."""
    return 2 * (width + height)


def calc_area_of_circle(radius):
    """Area of a circle."""
    return PI * radius**2


def calc_circumference_of_circle(radius):
    """Circumference (perimeter) of a circle."""
    return TAU * radius


def _has_positive_sides(a, b, c):
    return a > 0 and b > 0 and c > 0


def _satisfies_triangle_inequality(a, b, c):
    return a + b > c and a + c > b and b + c > a


def _count_distinct_sides(a, b, c):
    return len({a, b, c})


def classify_triangle(a, b, c):
    """Classify a triangle by side lengths.

    Returns one of: 'equilateral', 'isosceles', 'scalene', 'not a triangle'.
    """
    if not _has_positive_sides(a, b, c):
        return NOT_A_TRIANGLE
    if not _satisfies_triangle_inequality(a, b, c):
        return NOT_A_TRIANGLE

    distinct_sides = _count_distinct_sides(a, b, c)
    if distinct_sides == 1:
        return EQUILATERAL
    if distinct_sides == 2:
        return ISOSCELES
    return SCALENE
