class Solution:
    def myAtoi(self, s: str) -> int:
        i, n = 0, len(s)

        # 1) Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # If empty (or only spaces)
        if i == n:
            return 0

        # 2) Sign
        sign = 1
        if s[i] == '+' or s[i] == '-':
            if s[i] == '-':
                sign = -1
            i += 1

        # 3) Convert digits (skipping leading zeros naturally)
        num = 0
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')

            # 4) Clamp on overflow BEFORE it happens
            if num > INT_MAX // 10 or (num == INT_MAX // 10 and digit > INT_MAX % 10):
                return INT_MAX if sign == 1 else INT_MIN

            num = num * 10 + digit
            i += 1

        return sign * num
