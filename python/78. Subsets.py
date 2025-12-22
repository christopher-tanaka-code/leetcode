from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(index: int):
            if index == len(nums):
                res.append(subset.copy())
                return

            # Exclude nums[index]
            backtrack(index + 1)

            # Include nums[index]
            subset.append(nums[index])
            backtrack(index + 1)
            subset.pop()

        backtrack(0)
        return res
