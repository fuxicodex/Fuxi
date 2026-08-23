"""Graph helpers with intentional bugs. Score = all tests pass."""
from collections import deque


def bfs(graph, start):
    """Return nodes reachable from start in BFS order. Graph is a dict of
    node -> list of neighbors."""
    if start not in graph:
        return []
    order = [start]
    seen = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph.get(node, []):
            if neighbor not in seen:
                seen.add(neighbor)
                order.append(neighbor)
                queue.append(neighbor)
    return order


def shortest_path(graph, start, goal):
    """Return the shortest path length (number of edges) or -1 if unreachable."""
    if start not in graph:
        return -1
    if start == goal:
        return 0
    visited = {start}
    queue = deque([(start, 0)])
    while queue:
        node, dist = queue.popleft()
        for neighbor in graph.get(node, []):
            if neighbor == goal:
                return dist + 1
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
    return -1


def has_cycle(graph):
    """Return True if the directed graph has a cycle."""
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {}

    def visit(node):
        color[node] = GRAY
        for neighbor in graph.get(node, []):
            state = color.get(neighbor, WHITE)
            if state == GRAY:
                return True
            if state == WHITE and visit(neighbor):
                return True
        color[node] = BLACK
        return False

    return any(color.get(node, WHITE) == WHITE and visit(node) for node in graph)
