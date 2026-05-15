from collections import defaultdict
from functools import lru_cache
from typing import List

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)

        positions = defaultdict(list)
        for i, ch in enumerate(ring):
            positions[ch].append(i)

        @lru_cache(None)
        def dp(ring_pos: int, key_index: int) -> int:
            if key_index == len(key):
                return 0

            target = key[key_index]
            best = float("inf")

            for next_pos in positions[target]:
                distance = abs(next_pos - ring_pos)
                rotate_steps = min(distance, n - distance)

                # rotate_steps + 1 press + remaining characters
                best = min(
                    best,
                    rotate_steps + 1 + dp(next_pos, key_index + 1)
                )

            return best

        return dp(0, 0)