import heapq
from collections import defaultdict
from typing import List

class DualHeap:
    def __init__(self, k: int):
        self.small = []
        self.large = []
        self.delayed = defaultdict(int)
        self.k = k
        self.small_size = 0
        self.large_size = 0

    def prune(self, heap):
        while heap:
            num = -heap[0] if heap is self.small else heap[0]
            if self.delayed[num] == 0:
                break
            self.delayed[num] -= 1
            if self.delayed[num] == 0:
                del self.delayed[num]
            heapq.heappop(heap)

    def balance(self):
        if self.small_size > self.large_size + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
            self.small_size -= 1
            self.large_size += 1
            self.prune(self.small)
        elif self.small_size < self.large_size:
            heapq.heappush(self.small, -heapq.heappop(self.large))
            self.small_size += 1
            self.large_size -= 1
            self.prune(self.large)

    def insert(self, num: int):
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
            self.small_size += 1
        else:
            heapq.heappush(self.large, num)
            self.large_size += 1
        self.balance()

    def erase(self, num: int):
        self.delayed[num] += 1

        if num <= -self.small[0]:
            self.small_size -= 1
            if num == -self.small[0]:
                self.prune(self.small)
        else:
            self.large_size -= 1
            if self.large and num == self.large[0]:
                self.prune(self.large)

        self.balance()

    def median(self) -> float:
        if self.k % 2:
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        dh = DualHeap(k)
        ans = []

        for i, num in enumerate(nums):
            dh.insert(num)

            if i >= k:
                dh.erase(nums[i - k])

            if i >= k - 1:
                ans.append(dh.median())

        return ans