from typing import List
from collections import defaultdict

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7

        cnt = defaultdict(int)
        for x, y in points:
            cnt[y] += 1

        pair_counts = []
        for m in cnt.values():
            if m >= 2:
                pair_counts.append((m * (m - 1) // 2) % MOD)

        ans = 0
        prefix = 0
        for p in pair_counts:
            ans = (ans + prefix * p) % MOD
            prefix = (prefix + p) % MOD

        return ans
