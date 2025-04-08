def minimumOperations(nums):
    num_counts = {}
    counts = 0
    operations = 0

    for num in nums:
        num_counts[num] = num_counts.get(num, 0) + 1
        if num_counts[num] == 2:
            counts += 1

    idx = 0

    while idx < len(nums):
        print(counts)
        if counts <= 0:
            break
        if idx + 2 >= len(nums):
            operations += 1
            break
        num_counts[nums[idx]] -= 1
        if num_counts[nums[idx]] == 1:
            counts -= 1
        num_counts[nums[idx + 1]] -= 1
        if num_counts[nums[idx + 1]] == 1:
            counts -= 1
        num_counts[nums[idx + 2]] -= 1
        if num_counts[nums[idx + 2]] == 1:
            counts -= 1
        operations += 1
        idx += 3

    return operations


def main():
    nums = [3, 7, 7, 3]
    print(minimumOperations(nums))


if __name__ == "__main__":
    main()
