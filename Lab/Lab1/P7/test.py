def rps(p1, p2):
    player1 = p1
    player2 = p2
    if p1 == "E" and p2 == "E":
        return "No"

    p1_score = 0
    p2_score = 0

    for index in range(len(player1)):
        if player1[index] == player2[index]:
            continue
        elif player1[index] == "R":
            if player2[index] == "S":
                p1_score += 1
            else:
                p2_score += 1
        elif player1[index] == "S":
            if player2[index] == "P":
                p1_score += 1
            else:
                p2_score += 1
        elif player1[index] == "P":
            if player2[index] == "R":
                p1_score += 1
            else:
                p2_score += 1

    print(f"P1: {p1_score}")
    print(f"P2: {p2_score}")


p1 = "E"
p2 = "E"

rps(p1, p2)
