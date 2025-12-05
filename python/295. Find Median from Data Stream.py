import heapq

class MedianFinder:

    def __init__(self):
        # max-heap for lower half (store negatives because Python has only min-heap)
        self.low = []
        # min-heap for upper half
        self.high = []

    def addNum(self, num: int) -> None:
        # Always push into max-heap first
        heapq.heappush(self.low, -num)

        # Ensure every element in low <= every element in high
        if self.low and self.high and (-self.low[0] > self.high[0]):
            val = -heapq.heappop(self.low)
            heapq.heappush(self.high, val)

        # Balance heap sizes: low can have 1 more than high
        if len(self.low) > len(self.high) + 1:
            val = -heapq.heappop(self.low)
            heapq.heappush(self.high, val)

        if len(self.high) > len(self.low):
            val = heapq.heappop(self.high)
            heapq.heappush(self.low, -val)

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return float(-self.low[0])
        return (-self.low[0] + self.high[0]) / 2.0
