from typing import List
from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Convert each row to a tuple and count occurrences
        row_count = Counter(tuple(row) for row in grid)

        result = 0

        # Check each column against the rows
        for col_index in range(n):
            col_tuple = tuple(grid[row_index][col_index] for row_index in range(n))
            if col_tuple in row_count:
                result += row_count[col_tuple]

        return result
