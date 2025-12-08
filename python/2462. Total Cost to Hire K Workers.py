from heapq import heappush, heappop

class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        n = len(costs)
        total = 0
        
        # Two heaps for the first and last candidates
        left_heap, right_heap = [], []
        left_idx, right_idx = 0, n - 1
        
        # Fill initial candidates from both ends
        for _ in range(candidates):
            if left_idx <= right_idx:
                heappush(left_heap, (costs[left_idx], left_idx))
                left_idx += 1
            if left_idx <= right_idx:
                heappush(right_heap, (costs[right_idx], right_idx))
                right_idx -= 1

        # Hire k workers
        for _ in range(k):
            # Choose the smaller cost (tie broken by index)
            if not right_heap or (left_heap and left_heap[0] <= right_heap[0]):
                cost, idx = heappop(left_heap)
                total += cost
                # Add next candidate from the left side
                if left_idx <= right_idx:
                    heappush(left_heap, (costs[left_idx], left_idx))
                    left_idx += 1
            else:
                cost, idx = heappop(right_heap)
                total += cost
                # Add next candidate from the right side
                if left_idx <= right_idx:
                    heappush(right_heap, (costs[right_idx], right_idx))
                    right_idx -= 1

        return total
