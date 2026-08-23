"""Models for a todo app."""
from dataclasses import dataclass


@dataclass
class Todo:
    id: int
    title: str
    done: bool = False
