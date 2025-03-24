days = 57
meetings = [[3, 49], [23, 44], [21, 56], [26, 55], [23, 52], [2, 9], [1, 48], [3, 31]]

free = days

meetings.sort(key=lambda x: x[0])

free -= meetings[0][1] - meetings[0][0] + 1
latest = meetings [0][1]

for i in range(1, len(meetings)):
    start = meetings[i][0]
    end = meetings[i][1]

    if start < latest:
        if end > latest:
            free -= end - latest
            latest = end
    if start > latest:
        free -= end - start + 1
        latest = end
    elif start == latest:
        free -= end - start
        latest = end

print(free)