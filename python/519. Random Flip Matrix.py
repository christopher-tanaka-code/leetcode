import random
from typing import List

class Solution:
    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.total = m * n
        self.remaining = self.total
        self.swaps = {}

    def flip(self) -> List[int]:
        rand_index = random.randint(0, self.remaining - 1)

        actual_index = self.swaps.get(rand_index, rand_index)

        self.remaining -= 1

        self.swaps[rand_index] = self.swaps.get(
            self.remaining,
            self.remaining
        )

        row = actual_index // self.n
        col = actual_index % self.n

        return [row, col]

    def reset(self) -> None:
        self.remaining = self.total
        self.swaps.clear()