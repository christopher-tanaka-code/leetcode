from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        
        seen = set()
        repeated = set()
        
        for i in range(len(s) - 9):
            seq = s[i:i + 10]
            if seq in seen:
                repeated.add(seq)
            else:
                seen.add(seq)
        
        return list(repeated)
