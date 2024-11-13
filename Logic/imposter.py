import sys
from collections import deque


def read_input():
    input = sys.stdin.read().split()
    iterator = iter(input)
    n, k = int(next(iterator)), int(next(iterator))
    votes_list = []
    for _ in range(n):
        C = int(next(iterator))
        votes = [int(next(iterator)) - 1 for _ in range(C)]
        votes_list.append(votes)
    return n, k, votes_list


def implication_graph(n, votes_list):
    adj = [[] for _ in range(n)]
    for voter, list in enumerate(votes_list):
        for person in list:
            adj[person].append(voter)
    return adj

def bfs(start, adj, n, k):
    visited = [False] * (n)
    q = deque()
    q.append(start)
    visited[start] = True
    imposter_count = 1

    while q:
        curr = q.popleft()
        for vote in adj[curr]:
            if visited[vote] == False:
                visited[vote] = True
                imposter_count += 1
                q.append(vote)
                if imposter_count > k:
                    return imposter_count
    return imposter_count

def main():
    n, k, votes_list = read_input()
    adj = implication_graph(n, votes_list)
    
    results = []
    for villager in range(n):
        imposter_count = bfs(villager, adj, n, k)
        if imposter_count <= k:
            results.append('0')
        else:
            results.append('1')
    for result in results:
        print(result)
    

if __name__ == "__main__":
    main()
