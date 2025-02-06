from collections import deque

isWater = [[0, 0, 1], [1, 0, 0], [0, 0, 0]]
row, col = len(isWater), len(isWater[0])
heights = [[0] * col for _ in range(row)]
visited = set()
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for i in range(len(isWater)):
    for j in range(len(isWater[0])):
        visited.add((i, j))
        if isWater[i][j] == 1:
            visited.discard((i, j))
            for d in directions:
                x, y = d
                if 0 <= x + i < row and 0 <= y + j < col:
                    heights[x + i][y + j] = 1
                    visited.discard((x + i, y + j))
print(visited)
