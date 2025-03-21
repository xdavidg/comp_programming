nums = [0, 1, 1, 1, 0, 0]
operations = 0

for i in range(len(nums) - 2):
    if nums[i] == 0:
        nums[i] = nums[i] ^ 1
        nums[i + 1] = nums[i + 1] ^ 1
        nums[i + 2] = nums[i + 2] ^ 1
        operations += 1

if nums[-1] == nums[-2] and nums[-1] == 1:
    print(operations)