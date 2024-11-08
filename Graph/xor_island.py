import sys
from collections import defaultdict


def read_input():
    input = sys.stdin.read().split()
    N = int(input[0])
    hats = list(map(int, input[1:N+1]))
    return N, hats


def find_all_triples(N, hats):
    triples = []
    hat_to_indices = defaultdict(list)
    for idx, hat in enumerate(hats):
        hat_to_indices[hat].append(idx)
    for A in range(N):
        for B in range(N):
            if B == A:
                continue
            C_val = hats[A] ^ hats[B]
            if C_val in hat_to_indices:
                for C in hat_to_indices[C_val]:
                    if C != A and C != B:
                        triples.append((A, B, C))
    return triples


def compute_days(N, hats):
    triples = find_all_triples(N, hats)
    if not triples:
        return 0
    islander_triples = defaultdict(set)
    for idx, (A, B, C) in enumerate(triples):
        islander_triples[A].add(idx)
        islander_triples[B].add(idx)
        islander_triples[C].add(idx)
    remaining_triples = set(range(len(triples)))
    degrees = [len(islander_triples[i]) for i in range(N)]
    days = 0
    while True:
        days += 1
        to_raise = [i for i in range(N) if degrees[i] == 1]
        if to_raise:
            return days
        if days > N:
            break
    return days


def main():
    N, hats = read_input()
    days = compute_days(N, hats)
    print(days)


if __name__ == "__main__":
    main()
