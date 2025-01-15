matrix = [[1, 2, 3], [-1, -2, -3], [1, 2, 3]]

n = len(matrix)
count = 0
smallest = float("inf")
total = 0

for i in range(n):
    for j in range(n):
        curr = matrix[i][j]
        if curr < 0:
            count += 1
        if abs(curr) < smallest:
            smallest = abs(curr)
        total += abs(curr)

if count % 2 == 0:
    print(total)
else:
    total -= 2 * abs(smallest)
    print(total)
