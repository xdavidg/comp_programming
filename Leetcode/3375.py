def minOperations(nums, k):
    nums.sort()

    if nums[0] < k:
        return -1

    unique_count = 0
    unique = set()

    for i in range(len(nums) - 1, -1, -1):
        if nums[i] not in unique:
            unique.add(nums[i])
            unique_count += 1

    if nums[0] == k:
        return unique_count - 1
    else:
        return unique_count


def main():
    nums = [5, 2, 5, 4, 5]
    k = 2
    minOperations(nums, k)


if __name__ == "__main__":
    main()
