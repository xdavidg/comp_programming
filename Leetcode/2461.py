nums = [1,5,4,2,9,9,9]
k = 3

curr = set()
max = -1
sum = 0

for i in range(len(nums)):
    if len(curr) < k:
        if nums[i] not in curr:
            print("here", nums[i])
            curr.add(nums[i])
            sum += nums[i]
            if sum > max:
                max = sum
        else:
            while nums[i] in curr:
                temp = nums[i - len(curr) + 1]
                print(temp)
                curr.remove(temp)
                sum -= temp
            curr.add(nums[i])
            sum += nums[i]
            if sum > max:
                max = sum

print(max)