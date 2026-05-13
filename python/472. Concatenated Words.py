from typing import List

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key=len)

        word_set = set()
        answer = []

        min_len = float("inf")
        max_len = 0

        for word in words:
            if self.canForm(word, word_set, min_len, max_len):
                answer.append(word)

            word_set.add(word)
            min_len = min(min_len, len(word))
            max_len = max(max_len, len(word))

        return answer

    def canForm(self, word: str, word_set: set, min_len: int, max_len: int) -> bool:
        if not word_set:
            return False

        n = len(word)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            start = max(0, i - max_len)
            end = i - min_len

            for j in range(start, end + 1):
                if dp[j] and word[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]