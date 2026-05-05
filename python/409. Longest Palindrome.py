class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        length = 0

        for ch in s:
            if ch in seen:
                seen.remove(ch)
                length += 2
            else:
                seen.add(ch)

        # If any character has an odd count, we can place one in the center
        if seen:
            length += 1

        return length