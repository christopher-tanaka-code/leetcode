from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Step 1: Find the maximum candies any kid currently has
        max_candies = max(candies)
        
        # Step 2: Check for each kid if they can have the greatest number of candies
        return [candy + extraCandies >= max_candies for candy in candies]
