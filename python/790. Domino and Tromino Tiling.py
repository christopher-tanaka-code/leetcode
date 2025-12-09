class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        full = [0] * (n + 1)
        partial = [0] * (n + 1)
        
        full[0], full[1] = 1, 1
        partial[0], partial[1] = 0, 0
        
        for i in range(2, n + 1):
            partial[i] = (partial[i-1] + full[i-2]) % MOD
            full[i] = (full[i-1] + full[i-2] + 2 * partial[i-1]) % MOD
        
        return full[n]
