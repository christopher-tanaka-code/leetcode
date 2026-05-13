from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            zeros = s.count("0")
            ones = len(s) - zeros

            # Traverse backward so each string is used at most once
            for z in range(m, zeros - 1, -1):
                for o in range(n, ones - 1, -1):
                    dp[z][o] = max(
                        dp[z][o],
                        dp[z - zeros][o - ones] + 1
                    )

        return dp[m][n]