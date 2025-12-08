from typing import List
import bisect

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()  # Sort potions for binary search
        n = len(potions)
        result = []

        for spell in spells:
            # Minimum potion strength needed to succeed with this spell
            min_needed = (success + spell - 1) // spell  # Ceiling division
            # Find the first potion >= min_needed
            idx = bisect.bisect_left(potions, min_needed)
            # Count of successful pairs
            result.append(n - idx)
        
        return result
