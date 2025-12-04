from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtrack(start: int, path: List[int]):
            # If the current combination is of size k, add it to the result
            if len(path) == k:
                result.append(path[:])
                return
            # Try each number from 'start' to 'n'
            for i in range(start, n + 1):
                path.append(i)           # choose
                backtrack(i + 1, path)  # explore
                path.pop()               # un-choose (backtrack)

        backtrack(1, [])
        return result
