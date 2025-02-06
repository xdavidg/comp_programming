from collections import Counter

nums = [2, 3, 4, 6, 8, 12]

products = Counter()
total = 0

for i in range(0, len(nums) - 1):
    for j in range(i + 1, len(nums)):
        product = nums[i] * nums[j]
        total += products[product] * 8
        products[product] += 1

print(total)
