from bisect import bisect_right
from typing import List

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Sort by end time
        events.sort(key=lambda x: x[1])
        n = len(events)

        ends = [events[i][1] for i in range(n)]

        # best_prefix[i] = best single-event value among events[0..i]
        best_prefix = [0] * n
        best = 0
        for i in range(n):
            best = max(best, events[i][2])
            best_prefix[i] = best

        ans = 0
        for s, e, v in events:
            # Option 1: take this event alone
            ans = max(ans, v)

            # Option 2: take best event that ends <= s-1 plus this one
            idx = bisect_right(ends, s - 1) - 1
            if idx >= 0:
                ans = max(ans, v + best_prefix[idx])

        return ans
