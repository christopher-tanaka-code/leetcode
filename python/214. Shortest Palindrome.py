class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev = s[::-1]
        combined = s + "#" + rev

        # KMP prefix table
        lps = [0] * len(combined)
        j = 0

        for i in range(1, len(combined)):
            while j > 0 and combined[i] != combined[j]:
                j = lps[j - 1]
            if combined[i] == combined[j]:
                j += 1
                lps[i] = j

        longest_pal_prefix = lps[-1]
        add = rev[:len(s) - longest_pal_prefix]
        return add + s
