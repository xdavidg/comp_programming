import sys
import numpy as np


def main():
    import sys
    import numpy as np

    input = sys.stdin.read().split()
    ptr = 0
    test_case = 1

    while ptr < len(input):
        b = int(input[ptr])
        c = int(input[ptr + 1])
        ptr += 2

        if b == 0 and c == 0:
            break

        # Initialize ranks array
        # Using int16 as c <= 2500 fits in 16 bits
        ranks = np.empty((b, c), dtype=np.int16)

        for i in range(b):
            ballot = list(map(int, input[ptr:ptr + c]))
            ptr += c
            # Assign the rank for each candidate
            # ranks[i, candidate] = position in ballot
            ranks[i, ballot] = np.arange(c, dtype=np.int16)

        # Initialize winner as -1 (no winner)
        winner = -1

        # Precompute half of ballots for comparison
        half_b = b / 2

        # Iterate over each candidate to check if it's a Condorcet winner
        for A in range(c):
            # Get the ranks of candidate A across all ballots
            A_ranks = ranks[:, A].reshape(b, 1)
            # Compare A's rank with all other candidates' ranks
            # This creates a boolean array where True means A is preferred over B in that ballot
            comparison = (A_ranks < ranks)
            # Sum the number of ballots where A is preferred over each candidate B
            counts = np.sum(comparison, axis=0)
            # Exclude self-comparison by setting counts[A] to a large number
            # So that it doesn't affect the Condorcet condition
            counts[A] = b + 1
            # Check if A beats all other candidates
            if np.all(counts > half_b):
                winner = A
                break

        # Output the result for the current test case
        if winner != -1:
            print(f"Case {test_case}: {winner}")
        else:
            print(f"Case {test_case}: No Condorcet winner")

        test_case += 1


if __name__ == "__main__":
    main()
