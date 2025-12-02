from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        s, e = newInterval
        i, n = 0, len(intervals)

        # 1) Add all intervals that end before newInterval starts
        while i < n and intervals[i][1] < s:
            res.append(intervals[i])
            i += 1

        # 2) Merge all intervals that overlap with newInterval
        while i < n and intervals[i][0] <= e:
            s = min(s, intervals[i][0])
            e = max(e, intervals[i][1])
            i += 1
        res.append([s, e])

        # 3) Add the rest
        while i < n:
            res.append(intervals[i])
            i += 1

        return res
