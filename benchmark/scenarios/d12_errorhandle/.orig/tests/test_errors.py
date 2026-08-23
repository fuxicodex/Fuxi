import pytest
from src.errors import safe_read, parse_int, divide


def test_safe_read_ok(tmp_path):
    p = tmp_path / "a.txt"
    p.write_text("hello")
    assert safe_read(str(p)) == "hello"


def test_safe_read_missing_returns_none(tmp_path):
    assert safe_read(str(tmp_path / "missing.txt")) is None


def test_parse_int_ok():
    assert parse_int("42") == 42
    assert parse_int("-7") == -7


def test_parse_int_invalid():
    with pytest.raises(ValueError):
        parse_int("abc")


def test_divide_ok():
    assert divide(10, 2) == 5.0


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
