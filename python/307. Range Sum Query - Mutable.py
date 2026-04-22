from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums[:]                  # keep current values
        self.bit = [0] * (self.n + 1)       # 1-indexed Fenwick tree

        for i, num in enumerate(nums):
            self._add(i + 1, num)

    def _add(self, index: int, delta: int) -> None:
        while index <= self.n:
            self.bit[index] += delta
            index += index & -index

    def _prefix_sum(self, index: int) -> int:
        total = 0
        while index > 0:
            total += self.bit[index]
            index -= index & -index
        return total

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        self._add(index + 1, delta)

    def sumRange(self, left: int, right: int) -> int:
        return self._prefix_sum(right + 1) - self._prefix_sum(left)