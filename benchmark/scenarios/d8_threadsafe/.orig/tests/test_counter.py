import threading
from src.counter import SafeCounter


def test_single_thread():
    c = SafeCounter()
    for _ in range(100):
        c.increment()
    assert c.get() == 100


def test_concurrent_increment():
    c = SafeCounter()
    threads = [threading.Thread(target=c.increment) for _ in range(1000)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert c.get() == 1000  # no lost updates


def test_concurrent_mixed():
    c = SafeCounter()
    def up():
        for _ in range(500):
            c.increment()
    def down():
        for _ in range(500):
            c.decrement()
    threads = [threading.Thread(target=up) for _ in range(2)] + \
              [threading.Thread(target=down) for _ in range(2)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert c.get() == 0


def test_has_lock_attribute():
    c = SafeCounter()
    # A correct thread-safe counter should expose a lock
    assert hasattr(c, '_lock') or hasattr(c, 'lock')
