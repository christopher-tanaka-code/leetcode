class StockSpanner:

    def __init__(self):
        # Stack will store pairs: (price, span)
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        
        # Pop elements from stack while the price at top <= current price
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        
        # Push the current price and its span to stack
        self.stack.append((price, span))
        
        return span
