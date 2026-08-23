from src.lru import LRUCache


def test_get_missing():
    c = LRUCache(2)
    assert c.get(1) == -1


def test_put_get():
    c = LRUCache(2)
    c.put(1, 100)
    c.put(2, 200)
    assert c.get(1) == 100
    assert c.get(2) == 200


def test_eviction():
    c = LRUCache(2)
    c.put(1, 100)
    c.put(2, 200)
    c.put(3, 300)  # evicts 1 (least recently used)
    assert c.get(1) == -1
    assert c.get(2) == 200
    assert c.get(3) == 300


def test_lru_order_after_get():
    c = LRUCache(2)
    c.put(1, 100)
    c.put(2, 200)
    c.get(1)        # 1 becomes recently used
    c.put(3, 300)   # evicts 2
    assert c.get(1) == 100
    assert c.get(2) == -1
    assert c.get(3) == 300


def test_update_existing():
    c = LRUCache(2)
    c.put(1, 100)
    c.put(1, 111)  # update, no eviction
    assert c.get(1) == 111
    assert len(c.cache) == 1


def test_capacity_one():
    c = LRUCache(1)
    c.put(1, 100)
    c.put(2, 200)
    assert c.get(1) == -1
    assert c.get(2) == 200
