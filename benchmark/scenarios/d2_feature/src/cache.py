"""Cache utilities."""

from functools import wraps


def memoize(func):
    """Cache function results keyed by the call arguments.

    Same arguments only compute the function once; subsequent calls return
    the cached value. Works for any hashable positional or keyword arguments.
    """
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items()))) if kwargs else args
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return wrapper
