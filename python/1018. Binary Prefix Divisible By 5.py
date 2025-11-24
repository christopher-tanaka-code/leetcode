from typing import List

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        cur_mod = 0
        
        for bit in nums:
            # Update the current prefix value modulo 5
            cur_mod = (cur_mod * 2 + bit) % 5
            
            # True if divisible by 5
            ans.append(cur_mod == 0)
        
        return ans
