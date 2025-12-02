from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        # Greedy: sort by interval end, shoot at the earliest possible end.
        points.sort(key=lambda p: p[1])

        arrows = 1
        shot_x = points[0][1]

        for start, end in points[1:]:
            if start > shot_x:          # current arrow can't hit this balloon
                arrows += 1
                shot_x = end            # shoot at this balloon's end

        return arrows
