from typing import List
from collections import defaultdict

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        idx = {v: i for i, v in enumerate(arr)}
        
        # dp[k][j] = length of longest fib-like subseq ending with arr[j], arr[k]
        dp = [defaultdict(int) for _ in range(n)]
        best = 0
        
        for k in range(n):
            for j in range(k):
                need = arr[k] - arr[j]          # want arr[i] = need
                if need < arr[j] and need in idx:
                    i = idx[need]
                    dp[k][j] = dp[j].get(i, 2) + 1
                    best = max(best, dp[k][j])
                # else: implicit length is 2 (not stored), since no valid predecessor
        
        return best if best >= 3 else 0
