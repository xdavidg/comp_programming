import sys


def read_input():
    input = sys.stdin.read().splitlines()
    n, k = map(int, input[0].strip().split())
    votes = []
    for i in range(1, n + 1):
        votes.append((map(int, input[i].strip().split())))
    return n, k, votes


def count_votes(n, votes):
    vote_count = {}
    for i in range(n):
        num_votes = votes[i]
        for j in range(num_votes):
            vote_count[i] = vote_count.get(i, 0) + 1


def bfs(n, k, votes):


def main():
    n, k, votes = read_input()
    print(votes)


if __name__ == "__main__":
    main()
