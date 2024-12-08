import sys


def solution():
    M = int(sys.stdin.readline())
    bitmask = 0

    for _ in range(M):
        cmd, *args = sys.stdin.readline().split()
        if cmd == "add":
            bitmask |= 1 << (int(args[0]) - 1)
        elif cmd == "remove":
            bitmask &= ~(1 << (int(args[0]) - 1))
        elif cmd == "check":
            sys.stdout.write("1\n" if bitmask & (1 << (int(args[0]) - 1)) else "0\n")
        elif cmd == "toggle":
            bitmask ^= 1 << (int(args[0]) - 1)
        elif cmd == "all":
            bitmask = (1 << 20) - 1
        elif cmd == "empty":
            bitmask = 0


solution()
