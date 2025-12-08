class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0  # position to place the next non-zero
        
        # First pass: move non-zero values forward
        for num in nums:
            if num != 0:
                nums[pos] = num
                pos += 1
        
        # Second pass: fill the rest with zeros
        while pos < len(nums):
            nums[pos] = 0
            pos += 1
