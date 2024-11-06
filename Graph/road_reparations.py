import sys


def read_input():
    input = sys.stdin.read().splitlines()
    n, m = map(int, input[0].strip().split())
    graph = {}
    for i in range(1, m + 1):
        city1, city2, cost = map(int, input[i].strip().split())
        if city1 not in graph:
            graph[city1] = {}
        graph[city1][city2] = cost
        if city2 not in graph:
            graph[city2] = {}
        graph[city2][city1] = cost
    return graph, n


class UnionFind:
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            self.parent[root2] = root1
            return True
        return False


def kruskal_mst(graph):
    edges = []
    for city1 in graph:
        for city2, cost in graph[city1].items():
            if city1 < city2:
                edges.append((cost, city1, city2))
    edges.sort()

    uf = UnionFind(graph.keys())
    mst = []
    total_cost = 0

    for cost, city1, city2 in edges:
        if uf.union(city1, city2):
            mst.append((cost, city1, city2))
            total_cost += cost
    return total_cost, mst


def main():
    graph, n = read_input()
    total_cost, mst = kruskal_mst(graph)
    if len(mst) == n - 1:
        print(total_cost)
    else:
        print("IMPOSSIBLE")


if __name__ == "__main__":
    main()
