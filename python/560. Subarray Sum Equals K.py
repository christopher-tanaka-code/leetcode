from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1  # empty prefix sum

        prefix = 0
        ans = 0

        for x in nums:
            prefix += x
            ans += count[prefix - k]   # number of earlier prefixes that make sum k
            count[prefix] += 1

        return ans
