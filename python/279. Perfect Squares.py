from math import isqrt

class Solution:
    def numSquares(self, n: int) -> int:
        # 1) If n is a perfect square -> 1
        if isqrt(n) ** 2 == n:
            return 1

        # 2) Legendre's three-square theorem reduction:
        #    Remove factors of 4. If reduced n % 8 == 7 -> answer is 4
        m = n
        while m % 4 == 0:
            m //= 4
        if m % 8 == 7:
            return 4

        # 3) Check if n can be written as sum of two squares -> 2
        r = isqrt(n)
        for a in range(1, r + 1):
            b2 = n - a * a
            b = isqrt(b2)
            if b * b == b2:
                return 2

        # 4) Otherwise -> 3 (by Lagrange's four-square theorem + steps above)
        return 3
