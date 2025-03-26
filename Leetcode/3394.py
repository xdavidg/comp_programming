n = 5
rectangles = [[0, 0, 1, 1], [2, 0, 3, 4], [0, 2, 2, 3], [3, 0, 4, 3]]

x_rec = [None] * len(rectangles)
y_rec = [None] * len(rectangles)

for i in range(len(rectangles)):
    x_rec[i] = (rectangles[i][0], rectangles[i][2])
    y_rec[i] = (rectangles[i][1], rectangles[i][3])

x_rec.sort()
y_rec.sort()

print(x_rec)
print(y_rec)

line_count = 0
high = -1

for i in range(len(x_rec) - 1):
    if x_rec[i][0] == x_rec[i + 1][0]:
        high = max(high, x_rec[i + 1][1])
    elif x_rec[i][0] < x_rec[i + 1][0]:
        if x_rec[i][1] <= x_rec[i + 1][0] and x_rec[i + 1][0] >= high:
            line_count += 1
            high = x_rec[i + 1][1]
            if line_count == 2:
                print(True)
                break
        else:
            high = max(high, x_rec[i][1])

line_count = 0
high2 = -1

for i in range(len(y_rec) - 1):
    if y_rec[i][0] == y_rec[i + 1][0]:
        high2 = max(high2, y_rec[i + 1][1])
    elif y_rec[i][0] < y_rec[i + 1][0]:
        if y_rec[i][1] <= y_rec[i + 1][0] and y_rec[i + 1][0] >= high2:
            line_count += 1
            high2 = y_rec[i + 1][1]
            if line_count == 2:
                print(True)
                break
        else:
            high2 = max(high2, y_rec[i][1])
