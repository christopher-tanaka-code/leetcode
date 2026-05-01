from collections import defaultdict
import random

class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.indices = defaultdict(set)

    def insert(self, val: int) -> bool:
        is_new = len(self.indices[val]) == 0

        self.nums.append(val)
        self.indices[val].add(len(self.nums) - 1)

        return is_new

    def remove(self, val: int) -> bool:
        if not self.indices[val]:
            return False

        # Get one index where val exists
        remove_idx = self.indices[val].pop()

        # Get last element
        last_val = self.nums[-1]
        last_idx = len(self.nums) - 1

        # Move last element into remove_idx
        self.nums[remove_idx] = last_val

        # Update indices for last_val
        self.indices[last_val].add(remove_idx)
        self.indices[last_val].discard(last_idx)

        # Remove last position from array
        self.nums.pop()

        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)