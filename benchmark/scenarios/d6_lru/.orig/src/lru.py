"""LRU Cache with intentional bugs. Score = all tests pass."""
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        return self.cache[key]  # BUG: does not mark as recently used

    def put(self, key, value):
        self.cache[key] = value  # BUG: no LRU eviction, no reorder
