import pytest
from src.jsonutil import parse, get, stringify


def test_parse_valid():
    assert parse('{"a": 1}') == {"a": 1}
    assert parse("[1,2,3]") == [1, 2, 3]


def test_parse_invalid_raises():
    with pytest.raises(ValueError):
        parse("{invalid")


def test_get_nested():
    d = {"a": {"b": {"c": 42}}}
    assert get(d, "a.b.c") == 42
    assert get(d, "a.b.missing", "x") == "x"
    assert get(d, "x.y.z") is None


def test_stringify():
    assert stringify({"a": 1}) == '{"a": 1}'
    assert stringify({"a": 1}, indent=2) == '{\n  "a": 1\n}'
