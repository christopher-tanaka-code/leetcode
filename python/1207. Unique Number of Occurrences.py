from collections import Counter
from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Count occurrences of each element
        count = Counter(arr)
        # Extract counts and check if all counts are unique
        occurrences = list(count.values())
        return len(occurrences) == len(set(occurrences))
