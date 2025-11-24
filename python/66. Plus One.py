from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Start from the last digit and move left
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits  # no further carry, done
            else:
                digits[i] = 0  # 9 + 1 = 10, set to 0 and carry 1
        
        # If we reach here, all digits were 9 (e.g., 9, 99, 999)
        # We now need an extra digit at the front
        return [1] + digits
