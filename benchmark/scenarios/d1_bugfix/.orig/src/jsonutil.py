"""JSON parser with intentional bugs. Score = all tests pass."""
import json


def parse(s):
    return json.loads(s)  # no validation


def get(d, key, default=None):
    return d.get(key, default)  # no nested path support


def stringify(obj, indent=None):
    return json.dumps(obj, indent=indent)
