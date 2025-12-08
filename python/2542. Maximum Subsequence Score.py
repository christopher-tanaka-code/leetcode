from typing import List
import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # Pair nums2 with nums1 and sort by nums2 descending
        pairs = sorted(zip(nums2, nums1), reverse=True)

        heap = []
        current_sum = 0
        max_score = 0

        for num2, num1 in pairs:
            # Add nums1 to a min-heap
            heapq.heappush(heap, num1)
            current_sum += num1

            # Keep heap size <= k
            if len(heap) > k:
                current_sum -= heapq.heappop(heap)

            # If we have exactly k elements, calculate score
            if len(heap) == k:
                max_score = max(max_score, current_sum * num2)

        return max_score
