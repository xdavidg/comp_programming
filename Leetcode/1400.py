s = "true"
k = 4
count = 0
pali_dict = {}


def canPalindrome(s):
    letter_count = {}
    count = 0
    for c in s:
        letter_count[c] = letter_count.get(c, 0) + 1
    for key in letter_count:
        if letter_count[key] < 2:
            count += 1
            if count >= 2:
                return False
    return True


for i in range(len(s)):
    word1 = s[i : i + 1]
    word2 = s[i + 1 : len(s)]
    if canPalindrome(word1) and canPalindrome(word2) and word1 not in pali_dict:
        pali_dict[word1] = 1
        count += 1
    if count >= k:
        print("True", count)
print("False", count)

