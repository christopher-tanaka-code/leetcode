import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))  # sort by required capital
        max_heap = []
        i = 0
        n = len(projects)

        for _ in range(k):
            # Push all affordable projects into the max-heap
            while i < n and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])  # max-heap via negative values
                i += 1
            
            # If no projects are affordable
            if not max_heap:
                break
            
            # Choose the project with the largest profit
            w += -heapq.heappop(max_heap)

        return w
