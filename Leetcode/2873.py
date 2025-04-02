def maximimumTripletValue(nums):
    maxNum, maxDiff, maxTriplet = -1, -1, -1

    for x in range(len(nums)):
        maxTriplet = max(maxTriplet, maxDiff * nums[x])
        maxNum = max(maxNum, nums[x])
        maxDiff = max(maxDiff, maxNum - nums[x])

    return maxTriplet


def main():
    nums = [1, 10, 3, 4, 19]
    print(maximimumTripletValue(nums))


if __name__ == "__main__":
    main()
