from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)          # O(n)
        best = 0

        for x in s:
            # only start counting from "sequence starts"
            if x - 1 not in s:
                y = x
                while y in s:  # each number is visited at most once overall
                    y += 1
                best = max(best, y - x)

        return best
