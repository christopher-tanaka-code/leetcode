class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # Patterns like a*, a*b*, a*b*c* can match empty string
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        def matches(i: int, j: int) -> bool:
            # whether s[i-1] matches p[j-1] (assuming i>0, j>0)
            return p[j - 1] == '.' or s[i - 1] == p[j - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] != '*':
                    if matches(i, j):
                        dp[i][j] = dp[i - 1][j - 1]
                else:
                    # '*' can represent zero occurrences of p[j-2]
                    dp[i][j] = dp[i][j - 2]
                    # or one/more occurrences if p[j-2] matches s[i-1]
                    if matches(i, j - 1):
                        dp[i][j] = dp[i][j] or dp[i - 1][j]

        return dp[m][n]
