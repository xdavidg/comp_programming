from collections import defaultdict

s = "abaacbcbb"
frequency = [0] * 26
count = 0

for letter in s:
    frequency[ord(letter) - ord('a')] += 1

for freq in frequency:
    if freq == 0:
        continue
    if freq % 2 == 0:
        count += 2
    if freq % 2 == 1:
        count += 1

print(count)