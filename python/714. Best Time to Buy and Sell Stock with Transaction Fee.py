class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        cash, hold = 0, -prices[0]  # Initially, no stock: cash=0, hold=-prices[0]
        
        for price in prices[1:]:
            # Update cash and hold states
            cash = max(cash, hold + price - fee)  # sell stock today
            hold = max(hold, cash - price)       # buy stock today
        
        return cash
