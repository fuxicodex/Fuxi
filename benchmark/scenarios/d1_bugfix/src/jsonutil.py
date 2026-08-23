"""JSON parser with intentional bugs. Score = all tests pass."""
import json


def parse(s):
    try:
        return json.loads(s)
    except (json.JSONDecodeError, TypeError) as exc:
        raise ValueError(f"invalid JSON: {exc}") from exc


def get(d, key, default=None):
    cur = d
    for part in str(key).split("."):
        if isinstance(cur, dict) and part in cur:
            cur = cur[part]
        else:
            return default
    return cur


def stringify(obj, indent=None):
    return json.dumps(obj, indent=indent)
