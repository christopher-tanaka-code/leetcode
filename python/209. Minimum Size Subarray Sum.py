from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        window_sum = 0
        best = n + 1  # sentinel for "not found"
        
        for right, x in enumerate(nums):
            window_sum += x
            
            while window_sum >= target:
                best = min(best, right - left + 1)
                window_sum -= nums[left]
                left += 1
        
        return 0 if best == n + 1 else best
