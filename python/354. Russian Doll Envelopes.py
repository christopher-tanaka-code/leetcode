from typing import List
from bisect import bisect_left

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # Sort by width increasing.
        # If widths are equal, sort height decreasing.
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        lis = []

        for _, height in envelopes:
            idx = bisect_left(lis, height)

            if idx == len(lis):
                lis.append(height)
            else:
                lis[idx] = height

        return len(lis)