import heapq
import sys


def solution():
    N, D = map(int, sys.stdin.readline().split())
    shortcuts = [map(int, line.split()) for line in sys.stdin.read().splitlines()]

    # Initialize edges
    edges = dict()
    for i in range(D):
        edges[i] = [(i + 1, 1)]

    # Add shortcuts
    for shortcut in shortcuts:
        src, dst, distance = shortcut
        if dst <= D:
            edges[src].append((dst, distance))

    # Dijkstra
    distances = [float("inf")] * (D + 1)
    distances[0] = 0
    pq = [(0, 0)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # Reaches the destination
        if current_node == D:
            sys.stdout.write(str(current_distance) + "\n")
            return

        if current_distance > distances[current_node]:
            continue

        # Update the neighbors
        for dst, weight in edges[current_node]:
            distance = distances[dst]
            if current_distance + weight < distance:
                distances[dst] = current_distance + weight
                heapq.heappush(pq, (current_distance + weight, dst))

    sys.stdout.write(str(distances[D]) + "\n")


solution()
