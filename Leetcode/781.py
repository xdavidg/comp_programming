def numRabbits(answers):
    min_rabbit = 0
    unique = {}

    for i in range(len(answers)):
        if answers[i] == 0:
            min_rabbit += 1
        else:
            if answers[i] not in unique:
                unique[answers[i]] = unique.get(answers[i], 0) + 1
                min_rabbit += answers[i] + 1
            elif answers[i] - unique[answers[i]] < 0:
                unique[answers[i]] = 1
                min_rabbit += answers[i] + 1
            else:
                unique[answers[i]] = unique.get(answers[i], 0) + 1
        print(unique)
        print(min_rabbit)
    return min_rabbit


def main():
    answers = [0, 1, 0, 2, 0, 1, 0, 2, 1, 1]

    print(numRabbits(answers))


if __name__ == "__main__":
    main()
