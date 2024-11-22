text1 = "oxcpqrsvwf"
text2 = "shmtulqrypy"

n = len(text1) + 1
m = len(text2) + 1
matched = [False] * n

dp = [[0] * m for _ in range(n)]

for i, c in enumerate(text1):
    for j, d in enumerate(text2):
        if c == d:
            dp[i + 1][j + 1] = 1+ dp[i][j]
        else:
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

print(dp[-1][-1])