from collections import deque

grid = [[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]]
costs = {}
row, col = len(grid), len(grid[0])

directions = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}
dq = deque()
dq.append((0, 0, 0))
costs[(0, 0)] = 0

while dq:
    x, y, cost = dq.popleft()
    if (x, y) == (row - 1, col - 1):
        print(cost)

    for d in directions:
        n_cost = cost if d == grid[x][y] else cost + 1
        dx, dy = directions[d]
        nx, ny = x + dx, y + dy

        if (
            0 <= nx < row
            and 0 <= ny < col
            and n_cost < costs.get((nx, ny), float("inf"))
        ):
            if d == grid[x][y]:
                dq.appendleft((nx, ny))
            else:
                dq.append((nx, ny))
