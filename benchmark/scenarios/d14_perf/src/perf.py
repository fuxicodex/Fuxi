"""Optimized helpers. Behavior matches the original implementations."""


def fibonacci(n):
    # Iterative O(n), O(1) space.
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(n - 1):
        prev, curr = curr, prev + curr
    return curr


def find_duplicates(items):
    # O(n) via hash table; duplicates reported in order of first occurrence,
    # matching the original nested-loop ordering.
    counts = {}
    order = []
    for item in items:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
            order.append(item)
    return [item for item in order if counts[item] > 1]


def sum_range(n):
    # Closed-form O(1). Non-positive n sums nothing, as the original loop did.
    if n < 1:
        return 0
    return n * (n + 1) // 2
