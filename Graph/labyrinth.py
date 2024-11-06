from collections import deque
import sys


def read_input():
    input = sys.stdin.read().splitlines()
    n, m = map(int, input[0].split())
    grid = []
    start = end = None
    for i in range(1, n + 1):
        row = input[i]
        grid.append(row)
        if 'A' in row:
            start = (i - 1, row.index('A'))
        if 'B' in row:
            end = (i - 1, row.index('B'))
    return n, m, grid, start, end


def bfs(n, m, grid, start, end):
    visited = [[False] * m for _ in range(n)]
    predecessor = [[None] * m for _ in range(n)]

    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = True

    directions = [('U', -1, 0), ('D', 1, 0), ('L', 0, -1), ('R', 0, 1)]

    while queue:
        x, y = queue.popleft()

        if (x, y) == end:
            break

        for move, dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and grid[nx][ny] != '#':
                    visited[nx][ny] = True
                    predecessor[nx][ny] = (x, y, move)
                    queue.append((nx, ny))

    if not visited[end[0]][end[1]]:
        return None

    path = []
    x, y = end
    while (x, y) != start:
        prev = predecessor[x][y]
        px, py, move = prev
        path.append(move)
        x, y = px, py
    path.reverse()
    return ''.join(path)


def main():
    n, m, grid, start, end = read_input()
    path = bfs(n, m, grid, start, end)
    if path is None:
        print("NO")
    else:
        print("YES")
        print(len(path))
        print(path)


if __name__ == "__main__":
    main()
