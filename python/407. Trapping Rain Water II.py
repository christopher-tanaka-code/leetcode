from typing import List
import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])

        if m < 3 or n < 3:
            return 0

        visited = [[False] * n for _ in range(m)]
        min_heap = []

        # Add all boundary cells.
        # Boundary cells cannot trap water themselves.
        for r in range(m):
            for c in (0, n - 1):
                heapq.heappush(min_heap, (heightMap[r][c], r, c))
                visited[r][c] = True

        for c in range(1, n - 1):
            for r in (0, m - 1):
                heapq.heappush(min_heap, (heightMap[r][c], r, c))
                visited[r][c] = True

        water = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while min_heap:
            height, r, c = heapq.heappop(min_heap)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                if visited[nr][nc]:
                    continue

                visited[nr][nc] = True

                neighbor_height = heightMap[nr][nc]

                # If neighbor is lower than current boundary,
                # it can trap water up to height.
                if neighbor_height < height:
                    water += height - neighbor_height

                # The new boundary height is the max of current boundary
                # and this neighbor's own height.
                heapq.heappush(
                    min_heap,
                    (max(height, neighbor_height), nr, nc)
                )

        return water