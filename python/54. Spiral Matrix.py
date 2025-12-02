from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        res = []

        while top <= bottom and left <= right:
            # top row
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            top += 1

            # right column
            for r in range(top, bottom + 1):
                res.append(matrix[r][right])
            right -= 1

            # bottom row
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    res.append(matrix[bottom][c])
                bottom -= 1

            # left column
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    res.append(matrix[r][left])
                left += 1

        return res
