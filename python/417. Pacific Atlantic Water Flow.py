from typing import List
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        pacific_queue = deque()
        atlantic_queue = deque()

        pacific_seen = [[False] * n for _ in range(m)]
        atlantic_seen = [[False] * n for _ in range(m)]

        # Pacific touches top row and left column
        for r in range(m):
            pacific_queue.append((r, 0))
            pacific_seen[r][0] = True

        for c in range(n):
            pacific_queue.append((0, c))
            pacific_seen[0][c] = True

        # Atlantic touches bottom row and right column
        for r in range(m):
            atlantic_queue.append((r, n - 1))
            atlantic_seen[r][n - 1] = True

        for c in range(n):
            atlantic_queue.append((m - 1, c))
            atlantic_seen[m - 1][c] = True

        self.bfs(heights, pacific_queue, pacific_seen)
        self.bfs(heights, atlantic_queue, atlantic_seen)

        result = []

        for r in range(m):
            for c in range(n):
                if pacific_seen[r][c] and atlantic_seen[r][c]:
                    result.append([r, c])

        return result

    def bfs(self, heights: List[List[int]], queue: deque, seen: List[List[bool]]) -> None:
        m, n = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                if seen[nr][nc]:
                    continue

                # Reverse flow:
                # From ocean, move only to cells with height >= current height.
                if heights[nr][nc] >= heights[r][c]:
                    seen[nr][nc] = True
                    queue.append((nr, nc))