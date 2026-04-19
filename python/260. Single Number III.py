from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_all = 0
        for num in nums:
            xor_all ^= num

        diff_bit = xor_all & -xor_all

        a = 0
        b = 0

        for num in nums:
            if num & diff_bit:
                a ^= num
            else:
                b ^= num

        return [a, b]