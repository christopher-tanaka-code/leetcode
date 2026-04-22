from typing import List
from functools import lru_cache

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        @lru_cache(None)
        def dfs(r: int, c: int) -> int:
            best = 1  # path containing just this cell

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    best = max(best, 1 + dfs(nr, nc))

            return best

        ans = 0
        for r in range(rows):
            for c in range(cols):
                ans = max(ans, dfs(r, c))

        return ans