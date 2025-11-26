class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s

        best_l = best_r = 0  # inclusive indices

        def expand(l: int, r: int) -> None:
            nonlocal best_l, best_r
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            # went one step too far; palindrome is (l+1 .. r-1)
            l += 1
            r -= 1
            if r - l > best_r - best_l:
                best_l, best_r = l, r

        for i in range(n):
            expand(i, i)       # odd-length center
            expand(i, i + 1)   # even-length center

        return s[best_l:best_r + 1]
