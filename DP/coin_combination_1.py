in_list = list(map(int, input().strip().split(" ")))
num_coin = in_list[0]
total = in_list[1]

coin_list = list(map(int, input().strip().split(" ")))

mod = 1000000007

dp = [0] * (total + 1)
dp[0] = 1

for value in range(total + 1):
    for coin in coin_list:
        if value >= coin:
            dp[value] = (dp[value] + dp[value - coin]) % mod

print(dp[-1])
