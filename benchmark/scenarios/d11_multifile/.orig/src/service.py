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
        # MISSING: return todos that are not done
        raise NotImplementedError

    def done(self):
        # MISSING: return todos that are done
        raise NotImplementedError
