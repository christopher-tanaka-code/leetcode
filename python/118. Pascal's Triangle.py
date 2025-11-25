from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle: List[List[int]] = []
        
        for r in range(numRows):
            row = [1] * (r + 1)              # first and last are 1
            for i in range(1, r):            # fill middle entries
                row[i] = triangle[r - 1][i - 1] + triangle[r - 1][i]
            triangle.append(row)
        
        return triangle
