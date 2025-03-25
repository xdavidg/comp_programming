import heapq


def main():
    n = 7
    roads = [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3],
             [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]]

    g = [[] for _ in range(n)]

    for source, dest, cost in roads:
        g[source].append((dest, cost))
        g[dest].append((source, cost))

    dist = [float('inf')] * n
    ways = [0] * n
    mod = 10**9 + 7

    ways[0] = 1
    dist[0] = 0
    pq = [[0, 0]]

    while pq:
        d, node = heapq.heappop(pq)

        if d > dist[node]:
            continue

        for neighbour, time in g[node]:
            if dist[neighbour] > dist[node] + time:
                dist[neighbour] = dist[node] + time
                ways[neighbour] = ways[node]
                heapq.heappush(pq, (dist[neighbour], neighbour))
            elif dist[neighbour] == dist[node] + time:
                ways[neighbour] = (ways[neighbour] + ways[node]) % mod
    print(ways[n-1])


if __name__ == "__main__":
    main()
