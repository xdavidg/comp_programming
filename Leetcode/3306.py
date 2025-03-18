word = "aadieuoh"
k = 1

vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
consonant = 0
left = 0
total = 0

for right in range(len(word)):
    if word[right] in vowels:
        vowels[word[right]] += 1
    else:
        consonant += 1

    while consonant > k:
        if word[left] in vowels:
            vowels[word[left]] -= 1
        else:
            consonant -= 1
        left += 1

    if vowels['a'] > 0 and vowels['e'] > 0 and vowels['i'] > 0 and vowels['o'] > 0 and vowels['u'] > 0 and consonant == k:
        print(f"here {word[left:right + 1]}")
        total += 1

while vowels['a'] > 0 and vowels['e'] > 0 and vowels['i'] > 0 and vowels['o'] > 0 and vowels['u'] > 0 and consonant >= k:
    if word[left] in vowels:
        vowels[word[left]] -= 1
    else:
        consonant -= 1
    left += 1

    if vowels['a'] > 0 and vowels['e'] > 0 and vowels['i'] > 0 and vowels['o'] > 0 and vowels['u'] > 0 and consonant == k:
        print(f"there {word[left:right + 1]}")
        total += 1

print(total)
