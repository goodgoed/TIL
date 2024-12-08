def solution():
    N = int(input())

    prev = 1
    largest = -1
    layer = 0
    while True:
        largest = prev + 6 * layer
        if N >= prev and N <= largest:
            break
        prev = largest
        layer += 1

    print(layer + 1)


solution()
