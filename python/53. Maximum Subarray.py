from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize current sum and max sum
        current_sum = max_sum = nums[0]
        
        # Iterate through the array starting from index 1
        for num in nums[1:]:
            # Either extend the current subarray or start a new subarray
            current_sum = max(num, current_sum + num)
            # Update max_sum if current_sum is larger
            max_sum = max(max_sum, current_sum)
        
        return max_sum
