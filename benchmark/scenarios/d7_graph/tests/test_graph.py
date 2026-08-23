from src.graph import bfs, shortest_path, has_cycle


def test_bfs_simple():
    g = {0: [1, 2], 1: [3], 2: [3], 3: []}
    assert bfs(g, 0) == [0, 1, 2, 3]


def test_bfs_disconnected():
    g = {0: [1], 1: [], 2: []}
    assert bfs(g, 0) == [0, 1]


def test_bfs_missing_start():
    g = {0: [1], 1: []}
    assert bfs(g, 9) == []


def test_shortest_path():
    g = {0: [1, 2], 1: [3], 2: [3], 3: []}
    assert shortest_path(g, 0, 3) == 2
    assert shortest_path(g, 0, 0) == 0
    assert shortest_path(g, 3, 0) == -1


def test_has_cycle():
    g1 = {0: [1], 1: [2], 2: []}
    assert has_cycle(g1) is False
    g2 = {0: [1], 1: [2], 2: [0]}
    assert has_cycle(g2) is True
    g3 = {0: [1], 1: []}
    assert has_cycle(g3) is False
