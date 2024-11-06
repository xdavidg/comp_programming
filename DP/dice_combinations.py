n = int(input())
dice = 6
dp = [0] * (n + 1)
dp[0] = 1
mod = 1000000007

for j in range(1, n + 1):
    for i in range(1, dice + 1):
        if j >= i:
            dp[j] = (dp[j] + dp[j - i]) % mod

print(dp[-1])
