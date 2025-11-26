class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        # Overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine sign of result
        negative = (dividend < 0) ^ (divisor < 0)

        a = abs(dividend)
        b = abs(divisor)

        quotient = 0

        # Bitwise long division
        while a >= b:
            shift = 0
            # Find the largest shift such that (b << (shift+1)) <= a
            while a >= (b << (shift + 1)):
                shift += 1

            quotient += (1 << shift)
            a -= (b << shift)

        if negative:
            quotient = -quotient

        # Clamp to 32-bit range (mostly redundant due to overflow check, but safe)
        if quotient < INT_MIN:
            return INT_MIN
        if quotient > INT_MAX:
            return INT_MAX
        return quotient
