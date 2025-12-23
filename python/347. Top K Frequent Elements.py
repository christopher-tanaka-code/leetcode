from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)                 # O(n)
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, f in freq.items():          # O(#unique) <= O(n)
            buckets[f].append(num)

        res = []
        for f in range(len(nums), 0, -1):    # O(n)
            for num in buckets[f]:
                res.append(num)
                if len(res) == k:
                    return res
