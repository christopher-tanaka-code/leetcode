from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        jumps = 0
        end = 0
        farthest = 0

        for i in range(n - 1):  # stop before last index
            farthest = max(farthest, i + nums[i])

            if i == end:        # finished current jump range
                jumps += 1
                end = farthest
                if end >= n - 1:
                    break

        return jumps
