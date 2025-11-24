from typing import *

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Edge case: empty needle (classic definition)
        if needle == "":
            return 0
        
        n, m = len(haystack), len(needle)
        
        # No need to check if needle is longer than haystack
        if m > n:
            return -1
        
        # Slide over haystack
        for i in range(n - m + 1):
            # Compare substring of length m
            if haystack[i:i + m] == needle:
                return i
        
        # Not found
        return -1
