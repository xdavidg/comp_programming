from collections import deque


def maxPoints(grid, queries):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    answer = [0] * len(queries)
    i = 0

    for query in queries:
        dq = deque()
        dq.append((0, 0))
        result = 0
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        # base case if starting point is greater than query
        if grid[0][0] >= query:
            answer[i] = 0
            i += 1
            continue
        while dq:
            x, y = dq.popleft()
            if visited[x][y]:
                continue
            visited[x][y] = True
            result += 1
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < len(grid)
                    and 0 <= ny < len(grid[0])
                    and visited[nx][ny] == False
                    and query > grid[nx][ny]
                ):
                    dq.append((nx, ny))
        answer[i] = result
        i += 1
    return answer


def main():
    grid = [[1, 2, 3], [2, 5, 7], [3, 5, 1]]
    queries = [5, 6, 2]
    print(maxPoints(grid, queries))


if __name__ == "__main__":
    main()
