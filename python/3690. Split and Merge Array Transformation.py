from typing import List
from collections import deque

class Solution:
    def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:
        start = tuple(nums1)
        target = tuple(nums2)
        
        if start == target:
            return 0
        
        n = len(nums1)
        
        # BFS setup
        q = deque()
        q.append(start)
        dist = {start: 0}
        
        while q:
            cur = q.popleft()
            d = dist[cur]
            
            # Generate all neighbors by one split-and-merge operation
            for L in range(n):
                for R in range(L, n):
                    block = cur[L:R+1]
                    remaining = cur[:L] + cur[R+1:]
                    
                    m = len(remaining)
                    for pos in range(m + 1):
                        new_state = remaining[:pos] + block + remaining[pos:]
                        
                        # Skip no-op
                        if new_state == cur:
                            continue
                        
                        if new_state not in dist:
                            dist[new_state] = d + 1
                            if new_state == target:
                                return d + 1
                            q.append(new_state)
        
        # Theoretically unreachable if nums2 is a permutation of nums1, but:
        return -1
