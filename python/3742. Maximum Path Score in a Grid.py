from typing import List

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        # A path visits exactly m + n - 1 cells.
        # Since grid[0][0] == 0, max possible cost is at most m + n - 2.
        k = min(k, m + n - 2)

        NEG = -10**9

        # dp[j][c] = max score to reach current row's column j with exact cost c
        dp = [[NEG] * (k + 1) for _ in range(n)]

        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                cost = 0 if val == 0 else 1

                if i == 0 and j == 0:
                    dp[j] = [NEG] * (k + 1)
                    dp[j][0] = 0
                    continue

                cur = [NEG] * (k + 1)

                top = dp[j] if i > 0 else None
                left = dp[j - 1] if j > 0 else None

                for c in range(cost, k + 1):
                    prev_cost = c - cost
                    best_prev = NEG

                    if top is not None:
                        best_prev = max(best_prev, top[prev_cost])

                    if left is not None:
                        best_prev = max(best_prev, left[prev_cost])

                    if best_prev != NEG:
                        cur[c] = best_prev + val

                dp[j] = cur

        ans = max(dp[n - 1])
        return -1 if ans == NEG else ans