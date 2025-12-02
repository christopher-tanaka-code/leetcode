from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)          # required counts
        missing = len(t)           # total chars still missing (with duplicates)

        left = 0
        best_len = float("inf")
        best_l = 0

        for right, ch in enumerate(s):
            # If this char is still needed, we reduce missing.
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1  # negative means we have extra

            # When we've covered all chars, try to shrink from the left.
            while missing == 0:
                window_len = right - left + 1
                if window_len < best_len:
                    best_len = window_len
                    best_l = left

                left_ch = s[left]
                need[left_ch] += 1
                # If we just made a needed char missing again, stop shrinking.
                if need[left_ch] > 0:
                    missing += 1
                left += 1

        return "" if best_len == float("inf") else s[best_l:best_l + best_len]
