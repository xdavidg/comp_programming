num = int(input())

count = 0

i = 5

while num >= i:
    count += num // i
    i *= 5

print(count)
