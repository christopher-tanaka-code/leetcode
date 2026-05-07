from typing import List
from collections import defaultdict

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        answer = 0

        for x1, y1 in points:
            distance_count = defaultdict(int)

            for x2, y2 in points:
                dx = x1 - x2
                dy = y1 - y2
                distance = dx * dx + dy * dy

                distance_count[distance] += 1

            for count in distance_count.values():
                answer += count * (count - 1)

        return answer