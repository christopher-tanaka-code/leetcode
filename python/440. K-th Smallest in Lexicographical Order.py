class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        current = 1
        k -= 1

        while k > 0:
            steps = self.countSteps(n, current, current + 1)

            if steps <= k:
                # Skip this whole prefix subtree
                current += 1
                k -= steps
            else:
                # Go deeper into this prefix
                current *= 10
                k -= 1

        return current

    def countSteps(self, n: int, prefix1: int, prefix2: int) -> int:
        steps = 0

        while prefix1 <= n:
            steps += min(n + 1, prefix2) - prefix1
            prefix1 *= 10
            prefix2 *= 10

        return steps