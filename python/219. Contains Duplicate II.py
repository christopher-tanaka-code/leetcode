from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_index = {}  # value -> most recent index seen

        for i, x in enumerate(nums):
            if x in last_index and i - last_index[x] <= k:
                return True
            last_index[x] = i

        return False
