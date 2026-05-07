from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        third = float("-inf")

        for num in reversed(nums):
            # num is nums[i]
            # third is the best nums[k] found so far
            if num < third:
                return True

            # nums[j] must be greater than nums[k]
            while stack and num > stack[-1]:
                third = stack.pop()

            stack.append(num)

        return False