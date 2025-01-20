nums1 = [2, 1, 3]
nums2 = [10, 2, 5, 0]
bw_xor = 0

if len(nums1) % 2 == 0 and len(nums2) % 2 == 0:
    print(bw_xor)

elif len(nums1) % 2 == 0:
    for num in nums1:
        bw_xor = bw_xor ^ num
    print(bw_xor)

elif len(nums2) % 2 == 0:
    for num in nums2:
        bw_xor = bw_xor ^ num
    print(bw_xor)

else:
    for num1 in nums1:
        bw_xor = bw_xor ^ num1
    for num2 in nums2:
        bw_xor = bw_xor ^ num2
    print(bw_xor)