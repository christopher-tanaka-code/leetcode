class Solution:
    def numDecodings(self, s: str) -> int:
        # A string starting with '0' is invalid
        if not s or s[0] == '0':
            return 0

        # prev2 = ways to decode up to i-2
        # prev1 = ways to decode up to i-1
        prev2, prev1 = 1, 1

        for i in range(1, len(s)):
            current = 0

            # Single digit decode is valid if current char is not '0'
            if s[i] != '0':
                current += prev1

            # Two digit decode is valid if number is between 10 and 26
            two_digit = int(s[i - 1:i + 1])
            if 10 <= two_digit <= 26:
                current += prev2

            prev2, prev1 = prev1, current

        return prev1