from typing import List

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # dp_prev[j][r] = #ways to reach cell in previous row at column j
        # with path-sum % k == r
        dp_prev = [[0] * k for _ in range(n)]

        for i in range(m):
            dp_cur = [[0] * k for _ in range(n)]
            for j in range(n):
                v = grid[i][j] % k
                dest = dp_cur[j]

                if i == 0 and j == 0:
                    dest[v] = 1
                elif i == 0:
                    src = dp_cur[j - 1]  # only from left
                    for r in range(k):
                        dest[(r + v) % k] = src[r]
                elif j == 0:
                    src = dp_prev[j]     # only from top
                    for r in range(k):
                        dest[(r + v) % k] = src[r]
                else:
                    top = dp_prev[j]
                    left = dp_cur[j - 1]
                    for r in range(k):
                        dest[(r + v) % k] = (top[r] + left[r]) % MOD

            dp_prev = dp_cur

        return dp_prev[n - 1][0] % MOD
