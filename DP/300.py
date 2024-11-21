nums = [10, 9, 2, 5, 3, 7, 101, 18]
n = len(nums) + 1
dp = [0] * (n + 1)

prev = [0]


for i in range(1, n + 1):
    for j in range(i - 1, -1, -1):
        break