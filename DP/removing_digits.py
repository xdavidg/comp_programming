n = int(input())


def findMax(n):
    max = -1
    while n > 0:
        temp = n % 10
        if temp > max:
            max = temp
        n = n // 10
    return max


# print(findMax(n))

count = 0

while n >= 10:
    sub_num = findMax(n)
    n -= sub_num
    count += 1

print(count + 1)
