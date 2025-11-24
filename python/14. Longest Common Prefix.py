from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Since constraints say strs.length >= 1, this is safe,
        # but let's still guard for robustness
        if not strs:
            return ""
        
        # Start with the first string as the initial prefix
        prefix = strs[0]
        
        # Compare the prefix with each string
        for s in strs[1:]:
            # Shrink prefix until s starts with it or prefix becomes empty
            while prefix and not s.startswith(prefix):
                prefix = prefix[:-1]
            
            # Early exit: no common prefix
            if not prefix:
                return ""
        
        return prefix
