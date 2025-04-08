def mostPoints(questions):
    max_points = [0] * len(questions)

    for idx, value in reversed(list(enumerate(questions))):
        max = 0
        if idx + value[1] + 1 < len(max_points):
            max = max_points[idx + value[1] + 1]
        if idx + 1 < len(max_points) and max_points[idx + 1] > max + value[0]:
            max_points[idx] = max_points[idx + 1]
        else:
            max_points[idx] = max + value[0]

    return max_points[0]


def main():
    questions = [[3, 2], [4, 3], [4, 4], [2, 5]]
    print(mostPoints(questions))


if __name__ == "__main__":
    main()
