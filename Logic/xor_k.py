import sys


def read_input():
    input = sys.stdin.read().splitlines()
    n = int(input[0].strip())
    hats = [int(input[i]) for i in range(1, n + 1)]
    return n, hats


def calculate_xor(n, hats):
    xor_list = [[-1] * n for _ in range(n)]
    for i in range(len(hats)):
        for j in range(len(hats)):
            xor_list[i][j] = hats[i] ^ hats[j]
    return xor_list


def find_dats(xor_list):
    return


def main():
    n, hats = read_input()
    xor_list = calculate_xor(n, hats)
    print(xor_list)


if __name__ == "__main__":
    main()
