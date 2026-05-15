class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for length in range(2, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1

                if s[left] == s[right]:
                    dp[left][right] = 2 + dp[left + 1][right - 1]
                else:
                    dp[left][right] = max(
                        dp[left + 1][right],
                        dp[left][right - 1]
                    )

        return dp[0][n - 1]