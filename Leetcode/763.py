from collections import Counter


def partitionLabel(s):
    indexes = [[-1, -1] for _ in range(26)]
    counts = Counter(s)
    for i in range(len(s)):
        curr = len(indexes) - (ord("z") - ord(s[i])) - 1
        if indexes[curr][0] == -1:
            indexes[curr][0] = i
        counts[s[i]] = counts.get(s[i]) - 1
        if counts[curr] == 0:
            indexes[curr][1] = i

    idxs = []
    for x, y in indexes:
        if x != -1:
            idxs.append((x, y))
    idxs.sort()

    start, end = idxs[0][0], idxs[0][1]
    output = []
    print(idxs)

    for i in range(1, len(idxs)):
        if idxs[i][0] > end:
            output.append(end - start + 1)
            start = idxs[i][0]
            end = idxs[i][1]
        else:
            end = max(end, idxs[i][1])
    output.append(end - start + 1)
    return output


def main():
    s = "ababcbacadefegdehijhklij"
    print(partitionLabel(s))


if __name__ == "__main__":
    main()
