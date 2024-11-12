import sys
from collections import defaultdict, deque

def read_input():
    input = sys.stdin.read().split()
    iterator = iter(input)
    N, K = int(next(iterator)), int(next(iterator))
    
    non_imposter_lists = []
    for _ in range(N):
        C = int(next(iterator))
        non_imposters = [int(next(iterator)) - 1 for _ in range(C)]
        non_imposter_lists.append(non_imposters)
    
    return N, K, non_imposter_lists

def build_implications_graph(N, non_imposter_lists):

    adj = [[] for _ in range(N)]
    for A, non_imposters in enumerate(non_imposter_lists):
        for B in non_imposters:
            adj[B].append(A)
    return adj

def tarjan_scc(N, adj):

    index = 0
    indices = [-1] * N
    lowlink = [0] * N
    on_stack = [False] * N
    stack = []
    sccs = []

    def strongconnect(v):
        nonlocal index
        indices[v] = index
        lowlink[v] = index
        index += 1
        stack.append(v)
        on_stack[v] = True

        for neighbor in adj[v]:
            if indices[neighbor] == -1:
                strongconnect(neighbor)
                lowlink[v] = min(lowlink[v], lowlink[neighbor])
            elif on_stack[neighbor]:
                lowlink[v] = min(lowlink[v], indices[neighbor])

        if lowlink[v] == indices[v]:
            scc = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                scc.append(w)
                if w == v:
                    break
            sccs.append(scc)

    for v in range(N):
        if indices[v] == -1:
            strongconnect(v)

    return sccs

def build_dag(sccs, adj):
    scc_id_map = {}
    for idx, scc in enumerate(sccs):
        for villager in scc:
            scc_id_map[villager] = idx

    dag = [[] for _ in range(len(sccs))]
    for v in range(len(adj)):
        for w in adj[v]:
            if scc_id_map[v] != scc_id_map[w]:
                dag[scc_id_map[v]].append(scc_id_map[w])

    for edges in dag:
        unique_edges = list(set(edges))
        edges.clear()
        edges.extend(unique_edges)

    return dag, scc_id_map

def topological_sort(dag):

    num_nodes = len(dag)
    in_degree = [0] * num_nodes
    for edges in dag:
        for node in edges:
            in_degree[node] += 1

    queue = deque([node for node in range(num_nodes) if in_degree[node] == 0])
    topo_order = []

    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v in dag[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    return topo_order

def compute_closure_sizes(sccs, dag, topo_order):
    closure_size = [len(scc) for scc in sccs]

    for u in reversed(topo_order):
        for v in dag[u]:
            closure_size[u] += closure_size[v]

    return closure_size

def determine_imposters(N, K, scc_id_map, closure_size):
    results = []
    for villager in range(N):
        scc = scc_id_map[villager]
        if closure_size[scc] <= K:
            results.append('0')
        else:
            results.append('1')
    return results

def main():
    N, K, non_imposter_lists = read_input()
    adj = build_implications_graph(N, non_imposter_lists)
    sccs = tarjan_scc(N, adj)
    dag, scc_id_map = build_dag(sccs, adj)
    topo_order = topological_sort(dag)
    closure_size = compute_closure_sizes(sccs, dag, topo_order)
    results = determine_imposters(N, K, scc_id_map, closure_size)
    print('\n'.join(results))

if __name__ == "__main__":
    main()
