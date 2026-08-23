"""Inefficient helpers to optimize. Score = all tests pass (behavior preserved)."""


def fibonacci(n):
    # BUG: naive recursion, exponential time — must be O(n)
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def find_duplicates(items):
    # BUG: O(n^2) — must be O(n)
    result = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j] and items[i] not in result:
                result.append(items[i])
    return result


def sum_range(n):
    # BUG: O(n) loop — can be O(1), but must return correct result
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
