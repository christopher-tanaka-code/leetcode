from typing import List

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_xor = 0
        mask = 0

        # nums[i] <= 2^31 - 1, so check bits from 30 down to 0
        for bit in range(30, -1, -1):
            mask |= 1 << bit

            prefixes = set()
            for num in nums:
                prefixes.add(num & mask)

            candidate = max_xor | (1 << bit)

            # Check whether two prefixes can form this candidate XOR
            for prefix in prefixes:
                if prefix ^ candidate in prefixes:
                    max_xor = candidate
                    break

        return max_xor