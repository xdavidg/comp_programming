import sys
from collections import deque


def read_input():
    input = sys.stdin.read().splitlines()
    n, m = map(int, input[0].strip(" ").split())
    grid = [list(line.strip(" ")) for line in input[1:n+1]]
    return n, m, grid


def counting_rooms(n, m, grid):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def bfs(i, j):
        queue = deque()
        queue.append((i, j))
        grid[i][j] = '#'
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '.':
                    grid[nx][ny] = '#'
                    queue.append((nx, ny))

    room_count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.':
                bfs(i, j)
                room_count += 1
    return room_count


def main():
    n, m, grid = read_input()
    print(counting_rooms(n, m, grid))


if __name__ == "__main__":
    main()
