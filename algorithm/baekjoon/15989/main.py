import sys


def solution():
    N = int(sys.stdin.readline())
    nums = map(int, sys.stdin.read().splitlines())
    dp = [0] * 10001
    dp[0] = 1

    for i in [1, 2, 3]:
        for j in range(i, 10001):
            dp[j] += dp[j - i]

    for num in nums:
        sys.stdout.write(str(dp[num]) + "\n")


solution()
