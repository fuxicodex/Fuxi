"""Statistics helpers."""


def mean(values):
    if not values:
        raise ValueError("mean() arg is an empty sequence")
    return sum(values) / len(values)


def median(values):
    if not values:
        raise ValueError("median() arg is an empty sequence")
    ordered = sorted(values)
    n = len(ordered)
    mid = n // 2
    if n % 2:
        return ordered[mid]
    return (ordered[mid - 1] + ordered[mid]) / 2


def mode(values):
    if not values:
        raise ValueError("mode() arg is an empty sequence")
    return max(set(values), key=values.count)
