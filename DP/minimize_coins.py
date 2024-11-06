input_list = list(map(int, input().strip().split(" ")))

num_coins = input_list[0]
total = input_list[1]

coin_list = list(map(int, input().strip().split(" ")))

dp = [float('inf')] * (total + 1)
dp[0] = 0

for value in range(total + 1):
    for coin in coin_list:
        if value >= coin:
            temp = dp[value - coin] + 1
            if temp < dp[value]:
                dp[value] = temp

print(dp[-1] if dp[-1] != float('inf') else -1)
