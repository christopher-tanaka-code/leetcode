from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)  # Convert to set for O(1) lookups
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # Empty string can always be segmented

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # Found a valid split, no need to check further

        return dp[n]
