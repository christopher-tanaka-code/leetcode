from typing import List
from bisect import bisect_left

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        answer = 0

        for house in houses:
            pos = bisect_left(heaters, house)

            distance = float("inf")

            # Nearest heater on the right
            if pos < len(heaters):
                distance = min(distance, abs(heaters[pos] - house))

            # Nearest heater on the left
            if pos > 0:
                distance = min(distance, abs(house - heaters[pos - 1]))

            answer = max(answer, distance)

        return answer