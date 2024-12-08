import sys


def solution():
    N = int(sys.stdin.readline())
    requested_budgets = list(map(int, sys.stdin.readline().split()))
    total_budgets = sum(requested_budgets)
    remaining_budget = int(sys.stdin.readline())

    if total_budgets <= remaining_budget:
        sys.stdout.write(str(max(requested_budgets)) + "\n")
        return

    l, r = 0, max(requested_budgets)
    result = 0
    while l <= r:
        m = l + (r - l) // 2
        allocated_budget = 0

        for budget in requested_budgets:
            if budget > m:
                allocated_budget += m
            else:
                allocated_budget += budget

        if allocated_budget > remaining_budget:
            r = m - 1
        else:
            result = m
            l = m + 1

    sys.stdout.write(str(result) + "\n")


solution()
