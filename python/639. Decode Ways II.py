class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        if n == 0:
            return 0

        def ways1(ch: str) -> int:
            # number of ways to decode a single character
            if ch == '*':
                return 9
            if ch == '0':
                return 0
            return 1

        def ways2(a: str, b: str) -> int:
            # number of ways to decode two characters as a number 10..26
            if a == '*' and b == '*':
                # 11..19 (9) and 21..26 (6) => 15
                return 15
            if a == '*':
                # a can be '1' or '2' depending on b
                if '0' <= b <= '6':
                    return 2  # 10..16 or 20..26
                if '7' <= b <= '9':
                    return 1  # 17..19 only (a='1')
                return 0
            if b == '*':
                if a == '1':
                    return 9  # 11..19
                if a == '2':
                    return 6  # 21..26
                return 0
            # both digits
            val = (ord(a) - 48) * 10 + (ord(b) - 48)
            return 1 if 10 <= val <= 26 else 0

        dp0 = 1                 # dp[i-2]
        dp1 = ways1(s[0])       # dp[i-1] for i=1
        for i in range(1, n):
            cur = (dp1 * ways1(s[i]) + dp0 * ways2(s[i - 1], s[i])) % MOD
            dp0, dp1 = dp1, cur

        return dp1
