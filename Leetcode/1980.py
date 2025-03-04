nums = ["01", "10"]

unique = []
for i in range(len(nums)):
    if nums[i][i] == '1':
        unique.append('0')
    else:
        unique.append('1')
print(''.join(unique))
