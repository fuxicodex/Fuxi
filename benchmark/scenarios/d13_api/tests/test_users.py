import pytest
from src.users import UserService


def test_create_user():
    svc = UserService()
    u = svc.create_user("alice", "alice@example.com")
    assert u.id == 1
    assert u.name == "alice"
    assert u.email == "alice@example.com"


def test_create_duplicate_email_rejected():
    svc = UserService()
    svc.create_user("alice", "alice@example.com")
    with pytest.raises(ValueError):
        svc.create_user("bob", "alice@example.com")


def test_create_empty_name_rejected():
    svc = UserService()
    with pytest.raises(ValueError):
        svc.create_user("", "x@example.com")


def test_find_by_email():
    svc = UserService()
    svc.create_user("alice", "alice@example.com")
    svc.create_user("bob", "bob@example.com")
    assert svc.find_by_email("bob@example.com").name == "bob"
    assert svc.find_by_email("missing@example.com") is None


def test_get_missing_user():
    svc = UserService()
    assert svc.get_user(999) is None


def test_delete_user():
    svc = UserService()
    u = svc.create_user("alice", "alice@example.com")
    svc.delete_user(u.id)
    assert svc.get_user(u.id) is None
