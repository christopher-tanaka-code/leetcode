from typing import List

class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        ans = 0
        run = 0  # length of current alternating run ending at i

        for i, x in enumerate(nums):
            if i == 0 or nums[i] != nums[i - 1]:
                run += 1
            else:
                run = 1
            ans += run

        return ans
