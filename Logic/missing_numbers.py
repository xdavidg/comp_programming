def main():
    t = int(input().strip())
    s = input().strip()
    possibilites = []

    for i in range(1, 6):
        start, end = 0, i
        curr = int(s[:i])
        
        while end < len(s):
            
            if curr + 1 == next:
                start, end = i, i + i
            else:
                break
        if end == len(s) - 1:
            return True


if __name__ == "__main__":
    main()
