"""Bank account module with several bugs to find and fix (code review)."""


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("deposit amount must be non-negative")
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("withdraw amount must be non-negative")
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount

    def transfer(self, amount, other):
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount
        other.balance += amount

    def get_balance(self):
        return self.balance


class AccountManager:
    def __init__(self):
        self.accounts = {}

    def create_account(self, owner, balance=0):
        self.accounts[owner] = BankAccount(owner, balance)
        return self.accounts[owner]

    def get_account(self, owner):
        return self.accounts.get(owner, None)

    def total_deposits(self):
        return sum(a.balance for a in self.accounts.values())
