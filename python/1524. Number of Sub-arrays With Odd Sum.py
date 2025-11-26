from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        
        even = 1  # empty prefix sum
        odd = 0
        prefix = 0
        ans = 0
        
        for x in arr:
            prefix = (prefix + x) & 1  # parity only: 0 even, 1 odd
            
            if prefix == 1:
                ans += even
                odd += 1
            else:
                ans += odd
                even += 1
        
        return ans % MOD
