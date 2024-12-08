import sys


def solution():
    N = int(sys.stdin.readline())
    winner = "SK" if N % 2 != 0 else "CY"
    sys.stdout.write(winner + "\n")


solution()
