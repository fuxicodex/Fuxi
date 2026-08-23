"""Thread-safe counter."""
import threading


class SafeCounter:
    def __init__(self):
        self._value = 0
        self._lock = threading.Lock()

    @property
    def lock(self):
        return self._lock

    def increment(self):
        with self._lock:
            self._value += 1

    def decrement(self):
        with self._lock:
            self._value -= 1

    def get(self):
        with self._lock:
            return self._value
