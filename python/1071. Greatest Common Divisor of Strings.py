from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Step 1: Check concatenation property
        if str1 + str2 != str2 + str1:
            return ""
        
        # Step 2: Compute GCD of lengths
        length_gcd = gcd(len(str1), len(str2))
        
        # Step 3: Return prefix of str1 with length = gcd
        return str1[:length_gcd]
