import itertools


def numberOfArrays(differences, lower, upper):
    limit = upper - lower

    A = list(itertools.accumulate(differences, initial=0))
    print(A)

    diff = limit - (max(A) - min(A))

    return 0 if diff < 0 else diff + 1


def main():
    differences = [1, -3, 4]
    lower = 1
    upper = 6
    print(numberOfArrays(differences, lower, upper))


if __name__ == "__main__":
    main()
