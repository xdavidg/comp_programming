n = int(input())
nums = list(map(int, input().strip().split(" ")))

if n == 0:
    print("-1")

dp = [1] * (n + 1)

for i in range(1, n + 1):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
