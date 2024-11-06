input_str = input()

input_list = input_str.split(" ")
input_list = list(map(int, input_list))

coin_str = input()

coin_list = coin_str.split(" ")
coin_list = list(map(int, coin_list))


dp = [float('inf')] * (input_list[0] + 1)
dp[0] = 0

for index in range(1, len(dp)):
    for coin in coin_list:
        if index - coin >= 0:
            if dp[index] > dp[index - coin] + 1:
                dp[index] = dp[index - coin] + 1

if dp[-1] == float('inf'):
    print(-1)
else:
    print(dp[-1])