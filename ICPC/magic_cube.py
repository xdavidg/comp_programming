import sys

# read m, n and moves/queries list
# loop through m/q list backwards
#   if query -> add query list (array for order)
#   if move -> apply move to cube backwards
# print queries back to front


def read_input():
    input = sys.stdin.read().splitlines()
    n, m = map(int, input[0].split())
    instructions = []
    for i in range(1, m + 1):
        instructions.append(list(input[i].split()))
    return n, m, instructions


def main():
    n, m, instructions = read_input()
    queries = []
    for instruction in reversed(instructions):
        if instruction[0] == 'q':
            command, x, y, z = instruction
            queries.append((int(x), int(y), int(z)))
        else:
            plane, angle, index = instruction


if __name__ == "__main__":
    main()
