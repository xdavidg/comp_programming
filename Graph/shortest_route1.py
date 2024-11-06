import sys
import heapq


def read_input():
    input = sys.stdin.read().split()
    ptr = 0

    n = int(input[ptr])
    ptr += 1
    m = int(input[ptr])
    ptr += 1

    adj = [[] for _ in range(n + 1)]

    for _ in range(m):
        a = int(input[ptr])
        ptr += 1
        b = int(input[ptr])
        ptr += 1
        c = int(input[ptr])
        ptr += 1
        adj[a].append((b, c))

    return n, m, adj


def dijkstra(n, adj, start=1):
    dist = [float("inf")] * (n + 1)
    dist[start] = 0

    heap = [(0, start)]

    while heap:
        current_dist, city = heapq.heappop(heap)

        if current_dist > dist[city]:
            continue

        for city2, cost in adj[city]:
            if dist[city2] > dist[city] + cost:
                dist[city2] = dist[city] + cost
                heapq.heappush(heap, (dist[city2], city2))

    return dist


def main():
    n, m, adj = read_input()
    distances = dijkstra(n, adj, start=1)

    print(*distances[1:])


if __name__ == "__main__":
    main()
