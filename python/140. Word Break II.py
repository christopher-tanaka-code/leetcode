from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}

        def dfs(start: int) -> List[str]:
            if start == len(s):
                return [""]  # one valid way to finish

            if start in memo:
                return memo[start]

            sentences = []

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    rest_sentences = dfs(end)
                    for rest in rest_sentences:
                        if rest == "":
                            sentences.append(word)
                        else:
                            sentences.append(word + " " + rest)

            memo[start] = sentences
            return sentences

        return dfs(0)