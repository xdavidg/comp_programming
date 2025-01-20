arr = [6, 2, 3, 1, 4, 5]
mat = [[5, 1], [2, 4], [6, 3]]
hashmap = {}
r, c = len(mat[0]), len(mat)

for i in range(len(mat)):
    for j in range(len(mat[0])):
        hashmap[mat[i][j]] = (i, j)

p_row = {}
p_col = {}

for i in range(len(arr)):
    x, y = hashmap[arr[i]]
    p_row[x] = p_row.get(x, 0) + 1
    p_col[y] = p_col.get(y, 0) + 1
    if p_row[x] == r or p_col[y] == c:
        print(i)
        break
