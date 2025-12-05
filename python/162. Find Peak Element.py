class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # If middle < next element, peak is on the right side
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                # Peak is on the left side (including mid)
                right = mid
        
        # left == right, pointing to a peak
        return left
