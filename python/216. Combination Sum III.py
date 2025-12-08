from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def backtrack(start: int, path: List[int], remaining: int):
            # If the combination is of length k
            if len(path) == k:
                if remaining == 0:
                    result.append(path[:])  # Found a valid combination
                return

            # Try numbers from start to 9
            for i in range(start, 10):
                if i > remaining:  # Early pruning
                    break
                path.append(i)
                backtrack(i + 1, path, remaining - i)
                path.pop()  # Backtrack

        backtrack(1, [], n)
        return result
