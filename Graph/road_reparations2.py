def read_input():
    n, m = map(int, input().split())
    roads = []
    for _ in range(1, m + 1):
        a, b, c = map(int, input().split())
        roads.append((c, a, b))
    return n, m, roads


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size + 1))
        self.rank = [0] * (size + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)

        if xroot == yroot:
            return False

        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1

        return True


def main():
    n, m, roads = read_input()
    roads.sort()

    uf = UnionFind(n)
    total_cost = 0
    edges_used = 0

    for cost, a, b in roads:
        if uf.union(a, b):
            total_cost += cost
            edges_used += 1
            if edges_used == n - 1:
                break

    if edges_used == n - 1:
        print(total_cost)
    else:
        print("IMPOSSIBLE")


if __name__ == "__main__":
    main()
