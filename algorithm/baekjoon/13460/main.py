def solution():
    # Accepting input
    N, M = map(int, input().split())  # Read N and M

    # Reading the matrix
    matrix = [list(input().strip()) for _ in range(N)]

    # Find the location of R,B,O
    location = {"R": (-1, -1), "B": (-1, -1), "O": (-1, -1)}
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if matrix[i][j] == "R":
                location["R"] = (i, j)
            elif matrix[i][j] == "B":
                location["B"] = (i, j)
            elif matrix[i][j] == "O":
                location["O"] = (i, j)


def main():
    solution()


if __name__ == "__main__":
    main()
