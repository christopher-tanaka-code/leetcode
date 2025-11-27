from typing import List

class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        MOD = 10**9 + 7
        k = primeFactors

        if k == 1:
            return 1

        r = k % 3
        if r == 0:
            return pow(3, k // 3, MOD)
        if r == 1:
            # use one fewer 3: ... + 3 + 1  -> ... + 2 + 2
            return (pow(3, (k - 4) // 3, MOD) * 4) % MOD
        # r == 2
        return (pow(3, (k - 2) // 3, MOD) * 2) % MOD
