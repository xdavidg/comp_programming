def largestDivisibleSubset(nums):
    nums.sort()

    dp = [[] for _ in range(len(nums))]
    dp[0].append(nums[0])

    for i in range(1, len(nums)):
        largest = 0
        largest_idx = -1
        for j in range(i):
            if nums[i] % nums[j] == 0:
                if len(dp[j]) > largest:
                    largest = len(dp[j])
                    largest_idx = j
        if largest_idx != -1:
            for num in dp[largest_idx]:
                dp[i].append(num)
        dp[i].append(nums[i])

    print(dp)
    dp.sort(key=lambda x: len(x), reverse=True)
    return dp[0]


def main():
    nums = [4, 8, 10, 240]
    print(largestDivisibleSubset(nums))


if __name__ == "__main__":
    main()
