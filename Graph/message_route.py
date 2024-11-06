import sys
from collections import deque


def read_input():
    input = sys.stdin.read().splitlines()
    n, m = map(int, input[0].strip().split())
    adj = [[] for _ in range(n + 1)]
    for i in range(1, m + 1):
        x, y = map(int, input[i].strip().split())
        adj[x].append(y)
        adj[y].append(x)
    return n, m, adj


def bfs(n, adj):
    q = deque()
    visited = [False] * (n + 1)
    predecessor = [0] * (n + 1)
    q.append(1)
    visited[1] = True

    while q:
        city = q.popleft()
        for neighbour in adj[city]:
            if not visited[neighbour]:
                visited[neighbour] = True
                predecessor[neighbour] = city
                q.append(neighbour)

    return visited, predecessor


def main():
    n, m, adj = read_input()
    visited, predecessor = bfs(n, adj)
    if visited[-1] == False:
        print("IMPOSSIBLE")
    else:
        current = n
        path = []
        while current != 0:
            path.append(current)
            current = predecessor[current]
        path.reverse()
        print(len(path))
        print(*path)


if __name__ == "__main__":
    main()
