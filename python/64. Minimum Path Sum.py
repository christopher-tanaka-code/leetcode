from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        
        # DP table: reuse grid to save space
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue  # start point
                elif i == 0:
                    grid[i][j] += grid[i][j-1]  # only come from left
                elif j == 0:
                    grid[i][j] += grid[i-1][j]  # only come from top
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])  # min of top or left
        
        return grid[m-1][n-1]
