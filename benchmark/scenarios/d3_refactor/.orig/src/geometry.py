"""Messy module to be refactored. Behavior must be preserved (all tests pass),
but the code should be cleaner (remove duplication, improve names)."""


def calc_area_of_rectangle(w, h):
    a = w * h
    return a


def calc_perimeter_of_rectangle(w, h):
    p = 2 * (w + h)
    return p


def calc_area_of_circle(r):
    a = 3.141592653589793 * r * r
    return a


def calc_circumference_of_circle(r):
    c = 2 * 3.141592653589793 * r
    return c


def classify_triangle(a, b, c):
    # returns 'equilateral', 'isosceles', 'scalene', or 'not a triangle'
    if a <= 0 or b <= 0 or c <= 0:
        return "not a triangle"
    if a + b <= c or a + c <= b or b + c <= a:
        return "not a triangle"
    if a == b and b == c:
        return "equilateral"
    if a == b or b == c or a == c:
        return "isosceles"
    return "scalene"
