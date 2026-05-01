from typing import List

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        a %= MOD

        result = 1

        for digit in b:
            # If current exponent is x, after reading new digit d:
            # new exponent = x * 10 + d
            result = self.modPow(result, 10, MOD) * self.modPow(a, digit, MOD)
            result %= MOD

        return result

    def modPow(self, base: int, exp: int, mod: int) -> int:
        result = 1
        base %= mod

        while exp > 0:
            if exp % 2 == 1:
                result = (result * base) % mod

            base = (base * base) % mod
            exp //= 2

        return result