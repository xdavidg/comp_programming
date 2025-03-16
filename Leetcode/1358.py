s = "aaacb"

s_len = len(s)
total = 0
char_dict = {'a' : 0, 'b' : 0, 'c' : 0}
count = 0
left = 0

for right in range(s_len):
    if char_dict[s[right]] == 0:
        count += 1
    char_dict[s[right]] += 1
    while count == 3:
        total += s_len - right
        char_dict[s[left]] -= 1
        if char_dict[s[left]] == 0:
            count -= 1
        left += 1
print(total)
