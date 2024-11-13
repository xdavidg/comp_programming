def main():
    t = int(input().strip())
    s = input().strip()
    possibilites = []

    for i in range(1, 6):
        start, end = 0, i
        curr = int(s[:i])
        while end < len(possibilites):
            temp = str(curr + 1)
            start, end = i + 1, i + len(str)
            if end >= len(possibilites):
                break
            print(temp)
            print(s[start:end])
            if s[start:end] != temp:
                break


if __name__ == "__main__":
    main()
