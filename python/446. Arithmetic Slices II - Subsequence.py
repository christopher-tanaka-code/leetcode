from typing import List
from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)

        # dp[i][diff] = number of arithmetic subsequences ending at index i
        # with common difference diff and length at least 2
        dp = [defaultdict(int) for _ in range(n)]

        answer = 0

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]

                # Existing subsequences ending at j can be extended by nums[i]
                count = dp[j][diff]

                # Extending those creates valid subsequences of length >= 3
                answer += count

                # Add:
                # 1. all extended subsequences
                # 2. the new pair [nums[j], nums[i]]
                dp[i][diff] += count + 1

        return answer