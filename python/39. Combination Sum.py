from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(start, path, remaining):
            if remaining == 0:
                # Found a valid combination
                result.append(path[:])
                return
            if remaining < 0:
                # Exceeded the target
                return
            
            for i in range(start, len(candidates)):
                # Choose the number
                path.append(candidates[i])
                # Recurse, allowing the same number again
                backtrack(i, path, remaining - candidates[i])
                # Backtrack, remove the last number
                path.pop()
        
        backtrack(0, [], target)
        return result
