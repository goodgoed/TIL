import collections
import sys


def solution():
    N, M, start = map(int, sys.stdin.readline().split())
    edges = {}

    for edge in sys.stdin.read().splitlines():
        u, v = map(int, edge.split())
        edges[u] = edges.get(u, []) + [v]
        edges[v] = edges.get(v, []) + [u]

    for node, edge in edges.items():
        edge = sorted(edge, reverse=True)
        edges[node] = edge

    # DFS
    stack = [start]
    visited = set()
    while stack:
        node = stack.pop()
        if node in visited:
            continue

        if node in edges:
            stack.extend(edges[node])

        visited.add(node)
        sys.stdout.write(str(node) + " ")
    sys.stdout.write("\n")

    # BFS
    for node, edge in edges.items():
        edge = sorted(edge)
        edges[node] = edge

    queue = collections.deque([start])
    visited.clear()
    while queue:
        node = queue.popleft()
        if node in visited:
            continue

        if node in edges:
            queue.extend(edges[node])

        visited.add(node)
        sys.stdout.write(str(node) + " ")
    sys.stdout.write("\n")


solution()
