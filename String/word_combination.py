import sys

input = sys.stdin.read().splitlines()
target, k = input[0].strip(), int(input[1].strip())
word_dic = [[] for _ in range(26)]
for i in range(2, k + 2):
    sub = input[i].strip()
    if sub in target:
        end_letter = sub[-1]
        word_dic[ord(end_letter) - ord('a') + 1].append(sub)

dp = [0] * (len(target) + 1)
dp[0] = 1
mod = 1000000007

for i in range(1, len(target)):
    index = ord(target[i]) - ord('a') + 1
    print(index)
    for sub in word_dic[index]:
        if len(sub) <= i + 1:
            if sub == target[i - (len(sub)-1):i]:
                dp[i] = (dp[i] + dp[i-len(sub) + 1]) % mod

print(dp)
