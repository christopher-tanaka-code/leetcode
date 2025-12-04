from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = nums[0]
        max_sum = curr_max = nums[0]
        min_sum = curr_min = nums[0]
        
        for num in nums[1:]:
            # Standard Kadane for max subarray
            curr_max = max(num, curr_max + num)
            max_sum = max(max_sum, curr_max)
            
            # Modified Kadane for min subarray
            curr_min = min(num, curr_min + num)
            min_sum = min(min_sum, curr_min)
            
            # Keep track of total sum
            total += num
            
        # If all numbers are negative, max_sum is the answer
        if max_sum < 0:
            return max_sum
        
        # Maximum of non-circular and circular subarray sums
        return max(max_sum, total - min_sum)
