"""File/parse helpers with weak error handling. Score = all tests pass."""


def safe_read(path):
    """Return the file contents, or None if the file does not exist."""
    try:
        with open(path) as f:
            return f.read()
    except (FileNotFoundError, IsADirectoryError):
        return None


def parse_int(value):
    """Parse an int, raising ValueError with a clear message on bad input."""
    try:
        return int(value)
    except (TypeError, ValueError):
        raise ValueError(f"invalid integer value: {value!r}") from None


def divide(a, b):
    """Divide a by b, raising ZeroDivisionError when b is zero."""
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b
