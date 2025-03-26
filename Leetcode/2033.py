def minOperations(grid, x):

    values = sorted([val for row in grid for val in row])

    diff = [abs(val - values[0]) % x for val in values]
    if any(d != 0 for d in diff):
        return -1

    median = values[len(values) // 2]

    operations = sum(abs(val - median) // x for val in values)

    return operations


def main():
    grid = [[2, 4], [6, 8]]
    x = 2

    print(minOperations(grid, x))


if __name__ == "__main__":
    main()
