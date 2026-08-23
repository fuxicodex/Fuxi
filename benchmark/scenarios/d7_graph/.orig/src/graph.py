"""Graph helpers with intentional bugs. Score = all tests pass."""
from collections import deque


def bfs(graph, start):
    """Return nodes reachable from start in BFS order. Graph is a dict of
    node -> list of neighbors."""
    if start not in graph:
        return []
    visited = [start]
    queue = [start]
    while queue:
        node = queue.pop(0)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    return visited  # BUG: order is wrong for some graph shapes


def shortest_path(graph, start, goal):
    """Return the shortest path length (number of edges) or -1 if unreachable."""
    if start not in graph:
        return -1
    visited = set()
    queue = deque([(start, 0)])
    while queue:
        node, dist = queue.popleft()
        if node == goal:
            return dist
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph.get(node, []):
            queue.append((neighbor, dist + 1))
    return -1


def has_cycle(graph):
    """Return True if the directed graph has a cycle."""
    return False  # BUG: always returns False
