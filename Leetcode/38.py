def countAndSay(n):
    i = 1
    output = "1"

    while i < n:
        output = processString(output)
        i += 1
        print(output)
    return output


def processString(s):
    output = ""
    curr = 0
    cnt = 0

    while curr < len(s):
        cnt += 1
        if curr + 1 < len(s) and s[curr] == s[curr + 1]:
            curr += 1
        else:
            output += str(cnt) + s[curr]
            curr += 1
            cnt = 0
    return output


def main():
    print(countAndSay(4))


if __name__ == "__main__":
    main()
