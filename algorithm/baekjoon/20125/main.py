import sys


def solution():
    N = int(sys.stdin.readline())
    matrix = sys.stdin.read().splitlines()

    def find_head(matrix):
        for row in range(N):
            for col in range(N):
                if matrix[row][col] == "*":
                    return (row, col)

    head = find_head(matrix)
    heart = (head[0] + 1, head[1])
    heart_row, heart_col = heart
    sys.stdout.write(f"{heart_row + 1} {heart_col + 1}\n")

    left_arm = 0
    right_arm = 0

    for col in range(heart_col - 1, -1, -1):
        if matrix[heart_row][col] == "*":
            left_arm += 1
        else:
            break

    for col in range(heart_col + 1, N):
        if matrix[heart_row][col] == "*":
            right_arm += 1
        else:
            break

    waist = 0
    for row in range(heart_row + 1, N):
        if matrix[row][heart_col] == "*":
            waist += 1
        else:
            break

    left_leg = 0
    right_leg = 0
    for row in range(heart_row + waist + 1, N):
        if matrix[row][heart_col - 1] == "*":
            left_leg += 1
        if matrix[row][heart_col + 1] == "*":
            right_leg += 1

    sys.stdout.write(f"{left_arm} {right_arm} {waist} {left_leg} {right_leg}")


solution()
