class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Use a single row to save space (O(n) space)
        dp = [1] * n  # There's 1 way to reach any cell in the first row
        
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]  # current cell = from top + from left
                
        return dp[-1]
