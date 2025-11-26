from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        perim = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    perim += 4
                    # shared edge with right neighbor
                    if c + 1 < cols and grid[r][c + 1] == 1:
                        perim -= 2
                    # shared edge with down neighbor
                    if r + 1 < rows and grid[r + 1][c] == 1:
                        perim -= 2

        return perim
