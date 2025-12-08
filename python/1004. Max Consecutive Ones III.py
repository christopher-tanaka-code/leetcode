class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zeros = 0
        max_len = 0
        
        for right in range(len(nums)):
            # Count zeros in the window
            if nums[right] == 0:
                zeros += 1
            
            # Too many zeros → shrink from the left
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            # Update max window size
            max_len = max(max_len, right - left + 1)
        
        return max_len
