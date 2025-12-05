class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        # dp[i][j] will be the minimum operations to convert word1[0..i-1] to word2[0..j-1]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base cases: converting empty string to a string of length j requires j inserts
        for i in range(m + 1):
            dp[i][0] = i  # delete all characters from word1
        for j in range(n + 1):
            dp[0][j] = j  # insert all characters to word1
        
        # Fill the dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # no operation needed
                else:
                    # 1 + min(delete, insert, replace)
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],    # delete
                        dp[i][j - 1],    # insert
                        dp[i - 1][j - 1] # replace
                    )
        
        return dp[m][n]
