from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0  # Number of flowers we can plant
        length = len(flowerbed)
        
        for i in range(length):
            # Check if current plot is empty
            if flowerbed[i] == 0:
                # Check previous and next plots
                empty_prev = (i == 0) or (flowerbed[i - 1] == 0)
                empty_next = (i == length - 1) or (flowerbed[i + 1] == 0)
                
                # If both sides are empty, plant a flower here
                if empty_prev and empty_next:
                    flowerbed[i] = 1  # Plant the flower
                    count += 1
                    if count >= n:
                        return True
        
        return count >= n
