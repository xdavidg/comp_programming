from bisect import bisect_left

n = int(input().strip())
num_list = list(map(int, input().strip().split(" ")))

sub = []

for num in num_list:
    if len(sub) == 0 or sub[-1] < num:
        sub.append(num)
    else:
        idx = bisect_left(sub, num)
        sub[idx] = num

print(len(sub))
