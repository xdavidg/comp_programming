from collections import Counter

matrix = [[0, 0, 0], [0, 0, 1], [1, 1, 0]]

pat_freq = Counter()

for row in matrix:
    pattern = tuple(row) if row[0] == 0 else tuple(bit ^ 1 for bit in row)
    pat_freq[pattern] += 1

print(max(pat_freq.values()))
