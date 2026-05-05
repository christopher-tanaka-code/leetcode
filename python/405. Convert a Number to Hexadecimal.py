class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        hex_chars = "0123456789abcdef"

        # Convert negative numbers to 32-bit two's complement
        num &= 0xFFFFFFFF

        result = []

        while num > 0:
            digit = num & 0xF
            result.append(hex_chars[digit])
            num >>= 4

        return "".join(reversed(result))