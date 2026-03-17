from functools import lru_cache

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        @lru_cache(None)
        def dfs(a: str, b: str) -> bool:
            if a == b:
                return True

            # Prune: if character counts differ, impossible
            if sorted(a) != sorted(b):
                return False

            n = len(a)

            # Try every split position
            for i in range(1, n):
                # Case 1: no swap
                if dfs(a[:i], b[:i]) and dfs(a[i:], b[i:]):
                    return True

                # Case 2: swapped
                if dfs(a[:i], b[n - i:]) and dfs(a[i:], b[:n - i]):
                    return True

            return False

        return dfs(s1, s2)