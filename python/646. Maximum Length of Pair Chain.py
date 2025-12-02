from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])  # sort by right endpoint
        
        count = 0
        last_right = float("-inf")
        
        for left, right in pairs:
            if last_right < left:       # must satisfy b < c
                count += 1
                last_right = right
        
        return count
