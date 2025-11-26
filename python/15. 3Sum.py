from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 2):
            # Skip duplicate anchors
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Optional pruning: if the smallest possible sum is > 0, no more answers
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break
            # Optional pruning: if the largest possible sum is < 0, this i can't work
            if nums[i] + nums[n - 2] + nums[n - 1] < 0:
                continue

            l, r = i + 1, n - 1
            target = -nums[i]

            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    res.append([nums[i], nums[l], nums[r]])

                    l += 1
                    r -= 1

                    # Skip duplicates for l and r
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif s < target:
                    l += 1
                else:
                    r -= 1

        return res
