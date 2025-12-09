class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0
        
        # Sort intervals by their end time
        intervals.sort(key=lambda x: x[1])
        
        count = 0
        end = float('-inf')
        
        for interval in intervals:
            if interval[0] >= end:
                # No overlap, keep this interval
                end = interval[1]
            else:
                # Overlap, need to remove this interval
                count += 1
        
        return count
