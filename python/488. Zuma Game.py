from collections import Counter
from functools import lru_cache

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        colors = "RYBGW"
        INF = 10 ** 9
        hand_count = Counter(hand)

        def shrink(s: str) -> str:
            changed = True

            while changed:
                changed = False
                i = 0
                parts = []

                while i < len(s):
                    j = i
                    while j < len(s) and s[j] == s[i]:
                        j += 1

                    if j - i >= 3:
                        changed = True
                    else:
                        parts.append(s[i:j])

                    i = j

                s = "".join(parts)

            return s

        @lru_cache(None)
        def dfs(s: str, counts: tuple) -> int:
            if not s:
                return 0

            if sum(counts) == 0:
                return INF

            counts = list(counts)
            ans = INF

            for c_idx, c in enumerate(colors):
                if counts[c_idx] == 0:
                    continue

                counts[c_idx] -= 1

                for i in range(len(s) + 1):
                    if i > 0 and s[i - 1] == c:
                        continue

                    useful = False

                    if i < len(s) and s[i] == c:
                        useful = True

                    if 0 < i < len(s) and s[i - 1] == s[i] and s[i] != c:
                        useful = True

                    if not useful:
                        continue

                    new_s = shrink(s[:i] + c + s[i:])
                    sub = dfs(new_s, tuple(counts))

                    if sub != INF:
                        ans = min(ans, 1 + sub)

                counts[c_idx] += 1

            return ans

        result = dfs(shrink(board), tuple(hand_count[c] for c in colors))
        return -1 if result == INF else result