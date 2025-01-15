box = [
    ["#", "#", "*", ".", "*", "."],
    ["#", "#", "#", "*", ".", "."],
    ["#", "#", "#", ".", "#", "."],
]

n, m = len(box[0]), len(box)

flip = [["."] * m for _ in range(n)]

for i in range(m):
    pointer = n - 1
    for j in range(n - 1, -1, -1):
        if box[i][j] == "*":
            flip[j][m - 1 - i] = "*"
            pointer = j - 1
        elif box[i][j] == "#":
            flip[pointer][m - 1 - i] = "#"
            pointer = pointer - 1

print(box)
print(flip)
