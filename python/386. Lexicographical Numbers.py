from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        current = 1

        for _ in range(n):
            result.append(current)

            # Try to go deeper in lexicographical order:
            # 1 -> 10 -> 100 ...
            if current * 10 <= n:
                current *= 10
            else:
                # If we cannot go deeper, move to the next sibling.
                # If current ends with 9 or current + 1 > n,
                # climb back until we can move to the next valid number.
                while current % 10 == 9 or current + 1 > n:
                    current //= 10

                current += 1

        return result