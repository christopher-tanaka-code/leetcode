class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # lowercase English letters => frequency array is fastest
        freq = [0] * 26
        base = ord('a')

        for ch in s:
            freq[ord(ch) - base] += 1
        for ch in t:
            i = ord(ch) - base
            freq[i] -= 1
            if freq[i] < 0:   # early exit if t has extra of some letter
                return False

        return True
