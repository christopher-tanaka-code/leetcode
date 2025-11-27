from typing import List

class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        total = 0
        n = len(nums)

        for i, val in enumerate(nums):
            good = True

            if i - k >= 0 and val <= nums[i - k]:
                good = False
            if i + k < n and val <= nums[i + k]:
                good = False

            if good:
                total += val

        return total
