from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)

        while left < right:
            mid = (left + right) // 2

            if self.canSplit(nums, k, mid):
                right = mid
            else:
                left = mid + 1

        return left

    def canSplit(self, nums: List[int], k: int, max_allowed_sum: int) -> bool:
        subarrays = 1
        current_sum = 0

        for num in nums:
            if current_sum + num <= max_allowed_sum:
                current_sum += num
            else:
                subarrays += 1
                current_sum = num

                if subarrays > k:
                    return False

        return True