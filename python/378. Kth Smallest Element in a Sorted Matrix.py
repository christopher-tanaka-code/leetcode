from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        left = matrix[0][0]
        right = matrix[n - 1][n - 1]

        while left < right:
            mid = (left + right) // 2

            count = self.countLessOrEqual(matrix, mid)

            if count < k:
                left = mid + 1
            else:
                right = mid

        return left

    def countLessOrEqual(self, matrix: List[List[int]], target: int) -> int:
        n = len(matrix)
        row = n - 1
        col = 0
        count = 0

        while row >= 0 and col < n:
            if matrix[row][col] <= target:
                # Everything above matrix[row][col] in this column is <= target
                count += row + 1
                col += 1
            else:
                row -= 1

        return count