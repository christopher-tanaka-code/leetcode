from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])

        # dp[j] = max number of columns we can keep ending at column j
        dp = [1] * m

        for j in range(m):
            for i in range(j):
                # Can we place column j after column i for all rows?
                ok = True
                for r in range(n):
                    if strs[r][i] > strs[r][j]:
                        ok = False
                        break
                if ok:
                    dp[j] = max(dp[j], dp[i] + 1)

        best_keep = max(dp) if m > 0 else 0
        return m - best_keep
