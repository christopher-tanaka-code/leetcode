from typing import List
from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0: 1}

        for num in nums:
            nxt = defaultdict(int)

            for total, count in dp.items():
                nxt[total + num] += count
                nxt[total - num] += count

            dp = nxt

        return dp.get(target, 0)