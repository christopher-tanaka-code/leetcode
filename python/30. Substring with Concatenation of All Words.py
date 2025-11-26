from typing import List
from collections import Counter, defaultdict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        k = len(words[0])
        m = len(words)
        n = len(s)
        total_len = k * m
        if n < total_len:
            return []

        need = Counter(words)
        res = []

        # Try each alignment modulo k
        for offset in range(k):
            left = offset
            window = defaultdict(int)
            count = 0  # number of words currently in window (valid stream)

            # Move right in word-sized steps
            for right in range(offset, n - k + 1, k):
                w = s[right:right + k]

                if w in need:
                    window[w] += 1
                    count += 1

                    # Too many occurrences -> shrink
                    while window[w] > need[w]:
                        lw = s[left:left + k]
                        window[lw] -= 1
                        left += k
                        count -= 1

                    # Found a window with exactly m words
                    if count == m:
                        res.append(left)
                        # Slide forward by removing leftmost word
                        lw = s[left:left + k]
                        window[lw] -= 1
                        left += k
                        count -= 1
                else:
                    # Reset window if word not needed
                    window.clear()
                    count = 0
                    left = right + k

        return res
