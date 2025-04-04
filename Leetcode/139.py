def wordBreak(s, wordDict):
    for word in wordDict:
        if word in s:
            start = s.index(word)
            end = start + len(word)
            s = s[:start] + s[end:]
        else:
            return False
    return True


def main():
    s = "catsanddog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(wordBreak(s, wordDict))


if __name__ == "__main__":
    main()
