from collections import defaultdict


def countGood(nums, k):
    freq = defaultdict(int)
    left = 0
    counts = 0
    output = 0

    for right in range(len(nums)):
        counts += freq[nums[right]]
        freq[nums[right]] += 1

        while counts >= k:
            output += len(nums) - right
            freq[nums[left]] -= 1
            counts -= freq[nums[left]]
            left += 1
    return output


def main():
    nums = [3, 1, 4, 3, 2, 2, 4]
    k = 2
    print(countGood(nums, k))


if __name__ == "__main__":
    main()
