from collections import deque
from typing import List

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        queue = deque([(entrance[0], entrance[1], 0)])  # row, col, steps
        visited = set()
        visited.add((entrance[0], entrance[1]))

        while queue:
            row, col, steps = queue.popleft()
            
            # Check if current position is an exit (but not the entrance)
            if (row != entrance[0] or col != entrance[1]) and (row == 0 or row == m-1 or col == 0 or col == n-1):
                return steps
            
            # Explore neighbors
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < m and 0 <= c < n and maze[r][c] == '.' and (r, c) not in visited:
                    visited.add((r, c))
                    queue.append((r, c, steps + 1))
        
        return -1
