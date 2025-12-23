from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        i = 0
        while i < n:
            x = nums[i]
            # place x into its correct position x-1 if possible
            if 1 <= x <= n and nums[x - 1] != x:
                nums[i], nums[x - 1] = nums[x - 1], nums[i]
            else:
                i += 1

        # find first position where index doesn't match value
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
