from src.perf import fibonacci, find_duplicates, sum_range


def test_fibonacci_small():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(10) == 55


def test_fibonacci_large_fast():
    # O(n) is instant; naive recursion is visibly slow but terminates.
    assert fibonacci(30) == 832040


def test_find_duplicates():
    assert find_duplicates([1, 2, 3, 2, 4, 1]) == [1, 2]
    assert find_duplicates([1, 2, 3]) == []
    assert find_duplicates([]) == []


def test_find_duplicates_large_fast():
    # O(n) handles this instantly; O(n^2) is visibly slow.
    items = list(range(20000)) + [5, 5]
    assert find_duplicates(items) == [5]


def test_sum_range():
    assert sum_range(5) == 15
    assert sum_range(1) == 1
    assert sum_range(100) == 5050
