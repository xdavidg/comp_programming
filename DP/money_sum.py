n = int(input())

num_list = list(map(int, input().strip().split(" ")))

total = sum(num_list)

dp = [False] * (total + 1)
dp[0] = True

for coin in num_list:
    for sum in range(total, coin - 1, -1):
        if dp[sum - coin]:
            dp[sum] = True

possible_sum = [c for c in range(1, total + 1) if dp[c]]

print(len(possible_sum))
print(*possible_sum)
