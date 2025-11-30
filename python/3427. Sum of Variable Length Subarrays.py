from typing import List

class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        total = 0
        for i, val in enumerate(nums):
            start = max(0, i - val)
            total += prefix[i + 1] - prefix[start]

        return total
