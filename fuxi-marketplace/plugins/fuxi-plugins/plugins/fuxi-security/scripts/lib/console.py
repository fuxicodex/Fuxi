"""The scripts' console output: undecodable path names and failed removals, printed readably."""

from __future__ import annotations

import io
import sys


def tolerate_undecodable_names() -> None:
    """Make stdout print an undecodable path name as escapes instead of raising."""
    if isinstance(sys.stdout, io.TextIOWrapper):
        sys.stdout.reconfigure(errors="backslashreplace")


def removal_failure_detail(error: OSError) -> object:
    """The operator-readable reason a tree removal failed."""
    return str(error) if error.strerror or not error.args else error.args[0]
