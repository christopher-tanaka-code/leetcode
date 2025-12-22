from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total & 1:
            return False
        target = total // 2

        # bitset dp: bit i means sum i is achievable
        bits = 1  # sum 0 achievable
        for x in nums:
            bits |= bits << x
            # optional early exit
            if (bits >> target) & 1:
                return True

        return ((bits >> target) & 1) == 1
