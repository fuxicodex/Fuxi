"""Service layer for todos. Missing implementation."""
from .storage import TodoStore


class TodoService:
    def __init__(self, store=None):
        self.store = store or TodoStore()

    def create(self, title):
        if not title or not title.strip():
            raise ValueError("title must not be empty")
        return self.store.add(title.strip())

    def complete(self, todo_id):
        return self.store.complete(todo_id)

    def pending(self):
        return [t for t in self.store.list() if not t.done]

    def done(self):
        return [t for t in self.store.list() if t.done]
