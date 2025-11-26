from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        best_sum = nums[0] + nums[1] + nums[2]
        best_diff = abs(best_sum - target)

        for i in range(n - 2):
            # Optional pruning: skip duplicates for i (not required for correctness)
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                diff = abs(s - target)

                if diff < best_diff:
                    best_diff = diff
                    best_sum = s

                if s == target:
                    return s
                elif s < target:
                    l += 1
                else:
                    r -= 1

        return best_sum
