from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        
        for num in nums:
            # Update 'ones' and 'twos' using bitwise trick
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        
        return ones
