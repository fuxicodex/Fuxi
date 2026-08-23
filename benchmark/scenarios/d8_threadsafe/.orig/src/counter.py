"""Thread-safe counter with intentional bugs. Score = all tests pass."""
import threading


class SafeCounter:
    def __init__(self):
        self._value = 0
        # BUG: missing lock

    def increment(self):
        self._value += 1

    def decrement(self):
        self._value -= 1

    def get(self):
        return self._value
