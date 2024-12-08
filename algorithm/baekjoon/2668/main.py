import collections
import sys


def solution():
    N = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.read().splitlines()))
    result = []
    checked = [False for _ in range(N)]
    edges = collections.defaultdict(list)
    for i in range(N):
        edges[nums[i] - 1].append(i)

    def dfs(i, visited):
        visited.add(i)
        checked[i] = True

        for node in edges[i]:
            if node in visited:  # Cycle detected
                result.extend(visited)
                return
            elif not checked[node]:
                dfs(node, visited)

        visited.remove(i)

    for i in range(N):
        if not checked[i]:
            dfs(i, set())

    sys.stdout.write(str(len(result)) + "\n" + "\n".join(map(str, result)) + "\n")


solution()
