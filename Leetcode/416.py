def canPartition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False

    dp = [[False] * (total // 2 + 1) for _ in range(len(nums))]

    for i in range(len(dp)):
        dp[i][0] = True

    for i in range(len(nums)):
        for j in range(1, total // 2 + 1):
            if dp[i - 1][j] == True:
                dp[i][j] = True
            elif nums[i] > j:
                continue
            elif dp[i - 1][j - nums[i]] == True:
                dp[i][j] = True

    return dp[-1][-1]


def main():
    nums = [1, 5, 11, 5]
    print(canPartition(nums))


if __name__ == "__main__":
    main()
