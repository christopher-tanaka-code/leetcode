from typing import List

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        INF = 10**30
        min_pref = [INF] * k  # min prefix sum seen for each index % k
        min_pref[0] = 0       # pref[0] = 0 at index 0

        best = None
        pref = 0

        # j runs from 1..n (prefix positions), ensuring subarray is non-empty
        for j, x in enumerate(nums, start=1):
            pref += x
            r = j % k

            if min_pref[r] != INF:
                cand = pref - min_pref[r]
                best = cand if best is None else max(best, cand)

            # update min prefix for this remainder
            if pref < min_pref[r]:
                min_pref[r] = pref

        return best
