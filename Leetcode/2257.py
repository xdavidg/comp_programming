m = 4
n = 6
guards = [[0, 0], [1, 1], [2, 3]]
walls = [[0, 1], [2, 2], [1, 4]]

grid = [["."] * n for _ in range(m)]

for y, x in walls:
    grid[y][x] = "w"

for y, x in guards:
    grid[y][x] = "g"

for y, x in guards:
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    for dy, dx in directions:
        ny, nx = y, x
        while True:
            ny += dy
            nx += dx

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                break

            if grid[ny][nx] == "w" or grid[ny][nx] == "g":
                break

            grid[ny][nx] = "x"

count = 0

for i in range(m):
    for j in range(n):
        if grid[i][j] == ".":
            count += 1

print(count)
print(grid)
