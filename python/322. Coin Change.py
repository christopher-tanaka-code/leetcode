from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize DP array, dp[i] = fewest coins to make amount i
        # Set initial value to amount+1 (impossible large value)
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins needed to make amount 0

        # Build up the DP table
        for a in range(1, amount + 1):
            for coin in coins:
                if coin <= a:
                    dp[a] = min(dp[a], dp[a - coin] + 1)

        # If dp[amount] is still larger than amount, return -1
        return dp[amount] if dp[amount] <= amount else -1
