from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        need = total % p
        if need == 0:
            return 0

        last = {0: -1}  # remainder -> latest index where this remainder occurred
        pref = 0
        n = len(nums)
        best = n  # start with "impossible" meaning whole array

        for i, x in enumerate(nums):
            pref = (pref + x) % p
            target = (pref - need) % p

            if target in last:
                best = min(best, i - last[target])

            # store latest index (helps shorten length)
            last[pref] = i

        return -1 if best == n else best
