from typing import List

class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        d = distance

        for i in range(3, len(d)):
            # Case 1:
            # Current line crosses the line 3 steps before it.
            #
            # Example: [2, 1, 1, 2]
            if d[i] >= d[i - 2] and d[i - 1] <= d[i - 3]:
                return True

            # Case 2:
            # Current line overlaps the line 4 steps before it.
            #
            # Example: [1, 1, 2, 1, 1]
            if i >= 4:
                if d[i - 1] == d[i - 3] and d[i] + d[i - 4] >= d[i - 2]:
                    return True

            # Case 3:
            # Current line crosses the line 5 steps before it.
            #
            # Example: [1, 1, 2, 2, 1, 1]
            if i >= 5:
                if (
                    d[i - 2] >= d[i - 4]
                    and d[i] + d[i - 4] >= d[i - 2]
                    and d[i - 1] <= d[i - 3]
                    and d[i - 1] + d[i - 5] >= d[i - 3]
                ):
                    return True

        return False