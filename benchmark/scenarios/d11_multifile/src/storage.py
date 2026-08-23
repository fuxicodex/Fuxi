"""Storage layer for todos. Has a bug."""
from .models import Todo


class TodoStore:
    def __init__(self):
        self._items = {}
        self._next_id = 1

    def add(self, title):
        t = Todo(id=self._next_id, title=title)
        self._items[t.id] = t
        self._next_id += 1
        return t

    def get(self, todo_id):
        return self._items.get(todo_id)

    def list(self):
        return list(self._items.values())

    def complete(self, todo_id):
        t = self._items.get(todo_id)
        if t is None:
            return None
        t.done = True
        return t

    def delete(self, todo_id):
        return self._items.pop(todo_id, None)
