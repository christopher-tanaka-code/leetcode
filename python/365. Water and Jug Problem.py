from math import gcd

class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        # Cannot hold more water than both jugs combined
        if target > x + y:
            return False

        # If target is divisible by gcd(x, y), it is measurable
        return target % gcd(x, y) == 0