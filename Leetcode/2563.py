def countFairPairs(nums, lower, upper):
    nums.sort()

    def count_pairs(val):
        ans = 0
        j = len(nums) - 1
        for i in range(len(nums) - 1):
            while i < j and nums[i] + nums[j] > val:
                j -= 1
            if j > i:
                ans += j - i
        return ans

    return count_pairs(upper) - count_pairs(lower - 1)


def main():
    nums = [0, 1, 7, 4, 4, 5]
    lower = 3
    upper = 6
    print(countFairPairs(nums, lower, upper))


if __name__ == "__main__":
    main()
