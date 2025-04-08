from collections import Counter


def minimumIndex(nums):
    most_freq = Counter(nums).most_common(1)
    element, counts = most_freq[0][0], most_freq[0][1]

    if len(nums) // 2 > counts:
        return -1

    left = False
    l_count = 0
    i = 0

    while not left:
        if nums[i] == element:
            l_count += 1
            if (i + 1) // 2 < l_count:
                left = True
        i += 1

    remainder = counts - l_count
    if (len(nums) - i) // 2 < remainder:
        return i - 1
    else:
        return -1


def main():
    nums = [1, 2, 2, 2]
    print(minimumIndex(nums))


if __name__ == "__main__":
    main()
