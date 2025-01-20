from fractions import Fraction

digits = list(map(int, input()))
l = len(digits)
next_largest = [None] * l
stack = []

for i, d in reversed(list(enumerate(digits))):
    while stack and stack[-1][1] <= d:
        stack.pop()
    if stack:
        next_largest[i] = stack[-1][0]
    stack.append([i, d])

total, count = 0, 0

for i in range(len(digits)):
    count += l - i
    while next_largest[i]:
        total += (next_largest[i] - i) * digits[i]
        i = next_largest[i]
    total += (l - i) * digits[i]

if total / count == total // count:
    print(total // count)
elif total < count:
    num, den = Fraction(numerator=total %
                        count, denominator=count).as_integer_ratio()
    print(f"{num}/{den}")
else:
    num, den = Fraction(numerator=total %
                        count, denominator=count).as_integer_ratio()
    print(f"{total // count} {num} / {den}")
