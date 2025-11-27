from typing import List
from collections import defaultdict

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)

        # Smallest Prime Factor sieve up to n
        spf = list(range(n + 1))
        for i in range(2, int(n ** 0.5) + 1):
            if spf[i] == i:  # i is prime
                for j in range(i * i, n + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        def square_free(x: int) -> int:
            """Return square-free part of x."""
            res = 1
            while x > 1:
                p = spf[x]
                odd = 0
                while x % p == 0:
                    x //= p
                    odd ^= 1   # track parity of exponent
                if odd:
                    res *= p
            return res

        group_sum = defaultdict(int)
        for idx, val in enumerate(nums, start=1):  # 1-indexed
            key = square_free(idx)
            group_sum[key] += val

        return max(group_sum.values())
