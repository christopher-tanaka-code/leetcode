class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        # Sign
        sign = "-" if (numerator < 0) ^ (denominator < 0) else ""
        n, d = abs(numerator), abs(denominator)

        # Integer part
        integer_part = n // d
        remainder = n % d
        if remainder == 0:
            return sign + str(integer_part)

        # Fractional part via remainder tracking
        res = [sign + str(integer_part), "."]
        seen = {}  # remainder -> index in res where its digit starts

        while remainder != 0:
            if remainder in seen:
                idx = seen[remainder]
                res.insert(idx, "(")
                res.append(")")
                break

            seen[remainder] = len(res)
            remainder *= 10
            digit = remainder // d
            res.append(str(digit))
            remainder %= d

        return "".join(res)
