class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        max_len_ending_at = [0] * 26

        current_len = 0

        for i, ch in enumerate(s):
            if i > 0 and (ord(ch) - ord(s[i - 1])) % 26 == 1:
                current_len += 1
            else:
                current_len = 1

            idx = ord(ch) - ord("a")
            max_len_ending_at[idx] = max(max_len_ending_at[idx], current_len)

        return sum(max_len_ending_at)