from typing import List

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        # Build heights of consecutive 1s column by column
        for r in range(1, m):
            for c in range(n):
                if matrix[r][c] == 1:
                    matrix[r][c] += matrix[r - 1][c]

        ans = 0

        # For each row, sort heights descending to simulate best column rearrangement
        for r in range(m):
            heights = sorted(matrix[r], reverse=True)
            for i, h in enumerate(heights):
                ans = max(ans, h * (i + 1))

        return ans