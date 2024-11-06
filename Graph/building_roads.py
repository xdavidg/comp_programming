import sys
from collections import deque


def read_input():
    input = sys.stdin.read().splitlines()
    n, m = map(int, input[0].strip().split())
    adj = [[] for _ in range(n+1)]
    for i in range(1, m + 1):
        a, b = map(int, input[i].strip().split())
        adj[a].append(b)
        adj[b].append(a)
    return adj, n


def bfs(start, adj, visited):
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        city = queue.popleft()
        for city2 in adj[city]:
            if not visited[city2]:
                visited[city2] = True
                queue.append(city2)


def main():
    adj, n = read_input()
    representative = []
    visited = [False] * (n + 1)

    for city in range(1, n + 1):
        if not visited[city]:
            representative.append(city)
            bfs(city, adj, visited)

    additional_roads = len(representative) - 1
    print(additional_roads)
    for i in range(additional_roads):
        print(representative[i], representative[i + 1])


if __name__ == "__main__":
    main()
