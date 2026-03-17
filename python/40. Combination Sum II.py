from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        path = []

        def backtrack(start: int, remaining: int) -> None:
            if remaining == 0:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):
                # Skip duplicates at the same recursion level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Since array is sorted, no need to continue if too large
                if candidates[i] > remaining:
                    break

                path.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i])  # i + 1 because each number can be used once
                path.pop()

        backtrack(0, target)
        return result