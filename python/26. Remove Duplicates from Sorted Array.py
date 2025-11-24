from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Edge case: empty list (not needed per constraints, but good practice)
        if not nums:
            return 0
        
        # Index where the next unique element should go
        write = 1
        
        # Iterate from the second element
        for read in range(1, len(nums)):
            # If current element is different from the previous one, it's unique
            if nums[read] != nums[read - 1]:
                nums[write] = nums[read]
                write += 1
        
        # 'write' is the number of unique elements
        return write
