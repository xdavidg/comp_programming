class Solution:
    def stringMatching(self, words):
        ss = []
        words.sort(key = lambda word : len(word))

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[j] in words[i] and words[j] not in ss:
                    ss.append(words[j])
        return ss