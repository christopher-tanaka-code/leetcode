from typing import List
from collections import defaultdict

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stone_set = set(stones)
        last_stone = stones[-1]

        # jumps[position] = set of jump sizes that can land on this position
        jumps = defaultdict(set)
        jumps[0].add(0)

        for stone in stones:
            for last_jump in jumps[stone]:
                for next_jump in (last_jump - 1, last_jump, last_jump + 1):
                    if next_jump <= 0:
                        continue

                    next_stone = stone + next_jump

                    if next_stone == last_stone:
                        return True

                    if next_stone in stone_set:
                        jumps[next_stone].add(next_jump)

        return last_stone == 0