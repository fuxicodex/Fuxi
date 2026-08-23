"""A small math module. Your job is to WRITE DOCSTRINGS/type hints (documentation).
The code logic is already correct; do not change behavior, just document it."""


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


class Calculator:
    def __init__(self, initial=0):
        self.value = initial

    def add(self, n):
        self.value += n
        return self.value

    def reset(self):
        self.value = 0
        return self.value
