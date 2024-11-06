import sys
from collections import deque


def read_input():
    input = sys.stdin.read().splitlines()
    n, m = map(int, input[0].strip().split())
    grid = []
    monsters = []
    start = None

    for i in range(1, n + 1):
        row = list(input[i].strip())
        grid.append(row)

        for j, char in enumerate(row):
            if char == 'A':
                start = (i - 1, j)
            elif char == 'M':
                monsters.append((i - 1, j))
    return n, m, start, monsters, grid


def bfs_monsters(n, m, grid, monsters):
    monster_time = [[float('inf')] * m for _ in range(n)]
    q = deque()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for x, y in monsters:
        monster_time[x][y] = 0
        q.append((x, y))

    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = dx + x, dy + y
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != '#' and monster_time[nx][ny] == float('inf'):
                q.append((nx, ny))
                monster_time[nx][ny] = monster_time[x][y] + 1
    return monster_time


def is_boundary(x, y, n, m):
    if x == 0 or y == 0 or x == n - 1 or y == m - 1:
        return True


def bfs_player(n, m, grid, start, monster_time):
    player_time = [[float('inf')] * m for _ in range(n)]
    parent = [[None] * m for _ in range(n)]
    row, col = start
    q = deque()
    player_time[row][col] = 0
    directions = [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]
    q.append((row, col))
    path = ""

    if is_boundary(row, col, n, m):
        return True, path

    while q:
        x, y = q.popleft()
        for dx, dy, move in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != '#' and player_time[nx][ny] == float('inf'):
                new_time = player_time[x][y] + 1
                if new_time < monster_time[nx][ny]:
                    player_time[nx][ny] = new_time
                    parent[nx][ny] = (x, y, move)
                    if is_boundary(nx, ny, n, m):
                        path = []
                        cx, cy = nx, ny
                        while (cx, cy) != start:
                            px, py, pmove = parent[cx][cy]
                            path.append(pmove)
                            cx, cy = px, py
                        path.reverse()
                        return True, path
                    q.append((nx, ny))
    return False, None


def main():
    n, m, start, monsters, grid = read_input()
    monster_time = bfs_monsters(n, m, grid, monsters)
    possible, path = bfs_player(n, m, grid, start, monster_time)
    if possible:
        print('YES')
        print(len(path))
        print(''.join(path))
    else:
        print('NO')


if __name__ == "__main__":
    main()
