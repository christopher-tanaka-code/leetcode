from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Start with the last row
        dp = triangle[-1][:]
        
        # Iterate from second last row to top
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                # Update dp[j] with min path sum
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
        
        # The top element now contains the minimum path sum
        return dp[0]
