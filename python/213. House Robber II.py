from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_line(houses: List[int]) -> int:
            prev2 = 0  # dp[i-2]
            prev1 = 0  # dp[i-1]

            for money in houses:
                prev2, prev1 = prev1, max(prev1, prev2 + money)

            return prev1

        n = len(nums)

        if n == 1:
            return nums[0]

        # Either exclude the last house or exclude the first house
        return max(rob_line(nums[:-1]), rob_line(nums[1:]))
