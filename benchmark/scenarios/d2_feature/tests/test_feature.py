import pytest
from src.cache import memoize
from src.stats import mean, median, mode


def test_memoize_caches():
    calls = {"n": 0}

    @memoize
    def f(x):
        calls["n"] += 1
        return x * 2

    assert f(5) == 10
    assert f(5) == 10
    assert calls["n"] == 1  # cached


def test_memoize_distinct_args():
    @memoize
    def f(x):
        return x + 1

    assert f(1) == 2
    assert f(2) == 3


def test_mean():
    assert mean([1, 2, 3, 4]) == 2.5
    with pytest.raises(ValueError):
        mean([])


def test_median():
    assert median([1, 2, 3]) == 2
    assert median([1, 2, 3, 4]) == 2.5


def test_mode():
    assert mode([1, 2, 2, 3]) == 2
    with pytest.raises(ValueError):
        mode([])
