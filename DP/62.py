m = 3
n = 7

prev = [1] * n
curr = [1] * n

for i in range(1, m):
    for j in range(1, n):
        curr[j] = curr[j - 1] + prev[j]
    prev = curr
print(curr[-1])
    


