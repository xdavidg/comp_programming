from collections import deque

image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
color = 2
original = image[sr][sc]

row = len(image)
col = len(image[0])
boolean_graph = [[False] * col for i in range(row)]

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
dq = deque()
dq.append((sr, sc))
image[sr][sc] = color
boolean_graph[sr][sc] = True

while dq:
    x, y = dq.pop()
    for direction in directions:
        nx, ny = direction[0] + x, direction[1] + y
        if nx < row and nx >= 0 and ny < col and ny >= 0 and boolean_graph[nx][ny] == False and image[nx][ny] == original:
            boolean_graph[nx][ny] = True
            image[nx][ny] = color
            dq.append((nx, ny))
print(image)