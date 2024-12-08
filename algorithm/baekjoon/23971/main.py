import math


def solution():
    H, W, N, M = map(int, input().split())
    width = math.ceil(H / (N + 1))
    height = math.ceil(W / (M + 1))

    print(width * height)


solution()
