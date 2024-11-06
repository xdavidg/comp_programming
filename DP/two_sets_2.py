n = int(input())

mod = 10**9 + 7
n_sum = n * (n+1) // 2

if (n_sum) % 2 != 0:
    print(0)
else:
    target = n_sum // 2
    dp = [0] * (target + 1)
    dp[0] = 1

    for num in range(1, n + 1):
        for sum in range(target, num - 1, -1):
            dp[sum] = (dp[sum - num] + dp[sum]) % mod

    print(dp[target] // 2)
