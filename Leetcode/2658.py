from collections import deque

grid = [[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]
row, col = len(grid), len(grid[0])
fish_count = [[0] * col for _ in range(row)]
visited = [[False] * col for _ in range(row)]

max = 0
dq = deque()
dq.append((0, 0))
visited[0][0] = True
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while dq:
    x, y = dq.popleft()
    for d in directions:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < row and 0 <= ny < col:
            visited[nx][ny] = True
            dq.append((nx, ny))
            if grid[nx][ny] > 0:
                # bfs all paths storing visited so you dont add and then calculate those paths inidivudally
                break
