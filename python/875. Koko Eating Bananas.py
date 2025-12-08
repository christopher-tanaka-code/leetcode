from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Helper function to check if Koko can finish with speed k
        def can_finish(k: int) -> bool:
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            return hours <= h

        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if can_finish(mid):
                right = mid  # try smaller speed
            else:
                left = mid + 1  # need larger speed

        return left
