from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        m = n * n

        actual_sum = 0
        actual_sq_sum = 0
        for row in grid:
            for x in row:
                actual_sum += x
                actual_sq_sum += x * x

        S = m * (m + 1) // 2
        S2 = m * (m + 1) * (2 * m + 1) // 6

        diff1 = actual_sum - S              # a - b
        diff2 = actual_sq_sum - S2          # a^2 - b^2

        a_plus_b = diff2 // diff1           # (a+b)
        a = (diff1 + a_plus_b) // 2
        b = a - diff1

        return [a, b]
