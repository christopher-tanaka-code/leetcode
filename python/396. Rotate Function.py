from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)

        total_sum = sum(nums)

        # F(0)
        current = 0
        for i, num in enumerate(nums):
            current += i * num

        answer = current

        # Compute F(1), F(2), ..., F(n - 1)
        for k in range(1, n):
            current = current + total_sum - n * nums[n - k]
            answer = max(answer, current)

        return answer