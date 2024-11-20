s = "aaaaaaa"
wordDict = ["aaaa", "aaa"]
n = len(s)
max_len = max(map(len, wordDict))

dp = [0] * (n + 1)
dp[0] = 1

for i in range(1, n + 1):
    for j in range(i - 1, max(i - max_len, -1), -1):
        if s[j:i] in wordDict and dp[j]:
            dp[i] = True

