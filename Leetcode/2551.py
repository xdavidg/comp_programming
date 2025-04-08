w = [1, 3, 5, 1]
k = 2

p = sorted([w[i] + w[i + 1] for i in range(len(w) - 1)])
print(sum(p[len(p) - k + 1 :]) - sum(p[: k - 1]))
