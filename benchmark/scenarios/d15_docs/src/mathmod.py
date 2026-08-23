"""A small math module. Your job is to WRITE DOCSTRINGS/type hints (documentation).
The code logic is already correct; do not change behavior, just document it."""


def add(a, b):
    """Return the sum of two values.

    Args:
        a: The left operand. Any value supporting the ``+`` operator.
        b: The right operand. Any value that can be added to ``a``.

    Returns:
        The result of ``a + b``. For numbers this is their arithmetic sum;
        for sequences such as lists or strings it is their concatenation.
    """
    return a + b


def multiply(a, b):
    """Return the product of two values.

    Args:
        a: The left operand. Any value supporting the ``*`` operator.
        b: The right operand. Any value that can multiply ``a``.

    Returns:
        The result of ``a * b``. For numbers this is their arithmetic product;
        for a sequence and an integer it is the repeated sequence.
    """
    return a * b


class Calculator:
    """A tiny stateful accumulator.

    The calculator keeps a single running total in the ``value`` attribute.
    Operations mutate that total in place and return the updated result, so
    calls can be read as a running tally.

    Attributes:
        value: The current running total.
    """

    def __init__(self, initial=0):
        """Create a calculator with a starting total.

        Args:
            initial: The value to seed the running total with. Defaults to 0.
        """
        self.value = initial

    def add(self, n):
        """Add a value to the running total.

        Args:
            n: The amount to add to the current total.

        Returns:
            The updated running total after adding ``n``.
        """
        self.value += n
        return self.value

    def reset(self):
        """Clear the running total back to zero.

        Note that this resets to 0 regardless of the ``initial`` value the
        calculator was constructed with.

        Returns:
            The running total after the reset, which is always 0.
        """
        self.value = 0
        return self.value
