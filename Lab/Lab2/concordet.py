case_count = 1

while True:

    temp_in = input()

    in_list = temp_in.split(" ")
    in_list = list(map(int, in_list))

    if in_list[0] == in_list[1] and in_list[0] == 0:
        break

    candidate_scores = [0] * in_list[1]

    ballots = []

    for _ in range(in_list[0]):
        temp_ballot = input()
        temp_list = temp_ballot.split(" ")
        ballot = list(map(int, temp_list))
        ballots.append(ballot)

    for ballot in ballots:
        for index, value in enumerate(ballot):
            candidate_scores[value] += index

    min_score = float('inf')
    winner_index = -1
    tie_count = 0

    for index, score in enumerate(candidate_scores):
        if min_score > score:
            winner_index = index
            min_score = score
            tie_count = 0
        elif min_score == score:
            tie_count += 1

    if tie_count > 0:
        print(f"Case {case_count}: No Condorcet winner")
    else:
        print(f"Case {case_count}: {str(winner_index)}")

    case_count += 1
