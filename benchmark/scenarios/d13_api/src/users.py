"""User service API."""

import re

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


class User:
    def __init__(self, user_id, name, email):
        self.id = user_id
        self.name = name
        self.email = email


class UserService:
    def __init__(self):
        self._users = {}

    def create_user(self, name, email):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("name must be a non-empty string")
        if not isinstance(email, str) or not EMAIL_RE.match(email.strip()):
            raise ValueError(f"invalid email: {email!r}")

        name = name.strip()
        email = email.strip()
        if self.find_by_email(email) is not None:
            raise ValueError(f"email already registered: {email}")

        uid = len(self._users) + 1
        u = User(uid, name, email)
        self._users[uid] = u
        return u

    def get_user(self, user_id):
        return self._users.get(user_id)  # BUG: returns None, should raise KeyError?

    def find_by_email(self, email):
        for u in self._users.values():
            if u.email == email:
                return u
        return None

    def delete_user(self, user_id):
        # BUG: silently ignores missing user
        self._users.pop(user_id, None)
