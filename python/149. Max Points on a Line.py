from typing import List
from collections import defaultdict
from math import gcd

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        n = len(points)
        if n <= 2:
            return n

        max_points = 0

        for i in range(n):
            slopes = defaultdict(int)
            same_point = 1
            vertical = 0

            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]

                if dx == 0 and dy == 0:
                    same_point += 1
                elif dx == 0:
                    vertical += 1
                else:
                    g = gcd(dy, dx)
                    dy //= g
                    dx //= g
                    # Ensure unique representation for slope sign
                    if dx < 0:
                        dx, dy = -dx, -dy
                    slopes[(dy, dx)] += 1

            current_max = vertical  # Max points on vertical line
            if slopes:
                current_max = max(current_max, max(slopes.values()))
            max_points = max(max_points, current_max + same_point)

        return max_points
