from typing import List
import heapq


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Create events:
        #   entering event  -> (x, -height, right)
        #   leaving cleanup is handled lazily via heap using right edges
        events = []
        for left, right, height in buildings:
            events.append((left, -height, right))
            events.append((right, 0, 0))

        # Sort by x, then by height so starts are processed before ends,
        # and taller starts come first at the same x.
        events.sort()

        res = []
        # Max-heap simulated with negative heights.
        # Each entry is (-height, right)
        live = [(0, float("inf"))]

        for x, neg_h, right in events:
            # Remove buildings that ended before or at x
            while live and live[0][1] <= x:
                heapq.heappop(live)

            # Add new building if this is a start event
            if neg_h != 0:
                heapq.heappush(live, (neg_h, right))

            curr_height = -live[0][0]
            if not res or res[-1][1] != curr_height:
                res.append([x, curr_height])

        return res
