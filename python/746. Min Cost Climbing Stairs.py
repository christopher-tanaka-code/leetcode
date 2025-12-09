class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        # Initialize the first two steps
        first, second = cost[0], cost[1]
        
        # Compute the minimum cost iteratively
        for i in range(2, n):
            current = cost[i] + min(first, second)
            first, second = second, current
        
        # Minimum cost to reach the top (beyond the last step)
        return min(first, second)
