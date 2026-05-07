from typing import List
from bisect import bisect_left

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = []

        for index, interval in enumerate(intervals):
            starts.append((interval[0], index))

        starts.sort()

        sorted_start_values = [start for start, _ in starts]
        answer = []

        for start, end in intervals:
            pos = bisect_left(sorted_start_values, end)

            if pos == len(starts):
                answer.append(-1)
            else:
                answer.append(starts[pos][1])

        return answer