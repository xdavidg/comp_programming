derived = [1, 1, 0]

first = 0
last = 0

for n in derived:
    if n:
        last = ~last

print(first == last)