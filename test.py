words = ["hello", "goodbye", "zz", "z"]

ss = []
words.sort(key = lambda word : len(word), reverse = True)
print(words)

for i in range(len(words)):
    print(f"here is {i}")
    for j in range(i + 1, len(words)):
        print(j)
        if words[j] in words[i] and words[j] not in ss:
            ss.append(words[j])

print(ss)