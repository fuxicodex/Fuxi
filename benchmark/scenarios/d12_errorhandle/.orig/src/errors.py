"""File/parse helpers with weak error handling. Score = all tests pass."""


def safe_read(path):
    f = open(path)  # BUG: missing file should return None, not raise
    try:
        return f.read()
    finally:
        f.close()


def parse_int(value):
    return int(value)  # BUG: invalid input should raise ValueError with a clear message


def divide(a, b):
    if b == 0:
        return 0  # BUG: should raise ZeroDivisionError
    return a / b
