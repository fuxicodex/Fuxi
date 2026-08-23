import pytest
from src.bank import BankAccount, AccountManager


def test_deposit():
    a = BankAccount("alice")
    a.deposit(100)
    assert a.get_balance() == 100


def test_deposit_rejects_negative():
    a = BankAccount("alice", 100)
    with pytest.raises(ValueError):
        a.deposit(-50)
    assert a.get_balance() == 100


def test_withdraw():
    a = BankAccount("alice", 100)
    a.withdraw(40)
    assert a.get_balance() == 60


def test_withdraw_insufficient():
    a = BankAccount("alice", 100)
    with pytest.raises(ValueError):
        a.withdraw(200)
    assert a.get_balance() == 100


def test_transfer():
    a = BankAccount("alice", 100)
    b = BankAccount("bob", 0)
    a.transfer(40, b)
    assert a.get_balance() == 60
    assert b.get_balance() == 40


def test_transfer_insufficient():
    a = BankAccount("alice", 100)
    b = BankAccount("bob", 0)
    with pytest.raises(ValueError):
        a.transfer(200, b)
    assert a.get_balance() == 100


def test_account_manager():
    m = AccountManager()
    m.create_account("alice", 100)
    m.create_account("bob", 50)
    assert m.total_deposits() == 150
    assert m.get_account("alice").get_balance() == 100
    assert m.get_account("nonexistent") is None
