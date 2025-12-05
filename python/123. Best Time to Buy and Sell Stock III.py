from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        # Initialize variables:
        # t1_cost: min price for first buy
        # t1_profit: max profit after first sell
        # t2_cost: effective min price for second buy (price - t1_profit)
        # t2_profit: max profit after second sell
        t1_cost = float('inf')
        t2_cost = float('inf')
        t1_profit = 0
        t2_profit = 0
        
        for price in prices:
            # Minimize cost of first buy
            t1_cost = min(t1_cost, price)
            # Maximize profit after first sell
            t1_profit = max(t1_profit, price - t1_cost)
            # Minimize effective cost of second buy (consider first profit)
            t2_cost = min(t2_cost, price - t1_profit)
            # Maximize profit after second sell
            t2_profit = max(t2_profit, price - t2_cost)
        
        return t2_profit
