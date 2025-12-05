class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Handle negative powers
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1.0
        current_product = x
        
        while n > 0:
            # If n is odd, multiply the result by the current product
            if n % 2 == 1:
                result *= current_product
            # Square the current product
            current_product *= current_product
            # Divide n by 2
            n //= 2
        
        return result
