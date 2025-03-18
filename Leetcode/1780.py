import math

n = 6574365
distinct = set()

while (n > 0):
    print(n)
    if n < 3:
        a = 1
    else:
        a = 3**(int(math.log(n, 3)))
    if a in distinct:
        break
    n = n - a
    distinct.add(a)

if n == 0:
    print(f"True")
else:
    print(f"False, {n}")
    print(distinct)
