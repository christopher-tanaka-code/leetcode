from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path, remaining):
            if not remaining:  # If no elements left to add, we have a full permutation
                res.append(path[:])  # Append a copy of path
                return
            for i in range(len(remaining)):
                # Choose the current element
                path.append(remaining[i])
                # Explore with the remaining elements
                backtrack(path, remaining[:i] + remaining[i+1:])
                # Undo the choice (backtrack)
                path.pop()

        backtrack([], nums)
        return res
