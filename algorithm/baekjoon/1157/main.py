def solution():
    input_str = input()
    charSet = {}

    for s in input_str:
        s = s.upper()
        if s in charSet:
            charSet[s] += 1
        else:
            charSet[s] = 1

    maxChar, maxCount = "", 0
    for char, count in charSet.items():
        if count > maxCount:
            maxCount = count
            maxChar = char
        elif count == maxCount:
            maxChar = "?"

    print(maxChar)


solution()
