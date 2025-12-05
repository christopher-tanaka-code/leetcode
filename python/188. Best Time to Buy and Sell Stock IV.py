from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        
        # If k >= n//2, we can do unlimited transactions
        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit
        
        # DP approach: dp[i][j] = max profit up to day j with at most i transactions
        dp = [[0] * n for _ in range(k + 1)]
        
        for i in range(1, k + 1):
            max_diff = -prices[0]  # max(dp[i-1][m] - prices[m]) for m < j
            for j in range(1, n):
                dp[i][j] = max(dp[i][j - 1], prices[j] + max_diff)
                max_diff = max(max_diff, dp[i - 1][j] - prices[j])
        
        return dp[k][n - 1]
