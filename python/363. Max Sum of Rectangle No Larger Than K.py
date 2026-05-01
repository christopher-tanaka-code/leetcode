from typing import List
from bisect import bisect_left, insort

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        answer = float("-inf")

        # Use the smaller dimension for the pair loop.
        # This gives O(min(m, n)^2 * max(m, n) * log(max(m, n))).
        if m <= n:
            # Fix top and bottom rows, then reduce columns to 1D.
            for top in range(m):
                col_sums = [0] * n

                for bottom in range(top, m):
                    for col in range(n):
                        col_sums[col] += matrix[bottom][col]

                    answer = max(answer, self.maxSubarrayNoMoreThanK(col_sums, k))

                    if answer == k:
                        return k
        else:
            # Fix left and right columns, then reduce rows to 1D.
            for left in range(n):
                row_sums = [0] * m

                for right in range(left, n):
                    for row in range(m):
                        row_sums[row] += matrix[row][right]

                    answer = max(answer, self.maxSubarrayNoMoreThanK(row_sums, k))

                    if answer == k:
                        return k

        return answer

    def maxSubarrayNoMoreThanK(self, nums: List[int], k: int) -> int:
        prefix_sums = [0]
        current = 0
        best = float("-inf")

        for num in nums:
            current += num

            # Need smallest previous prefix >= current - k
            idx = bisect_left(prefix_sums, current - k)

            if idx < len(prefix_sums):
                best = max(best, current - prefix_sums[idx])

            insort(prefix_sums, current)

        return best