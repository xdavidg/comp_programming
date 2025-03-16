nums = [2, 3, 5, 9]
k = 2

def findMin(capability):
    count = 0
    i = 0

    while i <= len(nums):
        if nums[i] <= capability:
            count += 1
            i += 2
        else:
            i += 1
    return count >= k

left, right = min(nums), max(nums)

while left < right:
    mid = left + (right - left) // 2
    if findMin(mid):
        right = mid
    else:
        left = mid + 1
print(left)