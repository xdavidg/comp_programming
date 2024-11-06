info_list = list(map(int, input().strip().split(" ")))
num_coins = info_list[0]
total = info_list[1]

coin_list = list(map(int, input().strip().split(" ")))

dp = [0] * (total + 1)
dp[0] = 1
mod = 1000000007

for coin in coin_list:
    for value in range(1, total + 1):
        if value >= coin:
            dp[value] = (dp[value] + dp[value - coin]) % mod

print(dp[-1])
