from src.mathmod import add, multiply, Calculator


def test_add():
    assert add(2, 3) == 5


def test_multiply():
    assert multiply(4, 5) == 20


def test_calculator():
    c = Calculator(10)
    assert c.add(5) == 15
    assert c.reset() == 0
