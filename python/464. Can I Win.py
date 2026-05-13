from functools import lru_cache

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= 0:
            return True

        total_sum = maxChoosableInteger * (maxChoosableInteger + 1) // 2

        # Even if all numbers are chosen, target cannot be reached
        if total_sum < desiredTotal:
            return False

        @lru_cache(None)
        def dfs(used_mask: int, remaining: int) -> bool:
            for num in range(1, maxChoosableInteger + 1):
                bit = 1 << (num - 1)

                if used_mask & bit:
                    continue

                # Current player wins immediately
                if num >= remaining:
                    return True

                # If opponent loses after this move, current player wins
                if not dfs(used_mask | bit, remaining - num):
                    return True

            return False

        return dfs(0, desiredTotal)