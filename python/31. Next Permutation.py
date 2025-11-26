from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        if n <= 1:
            return

        # 1) Find pivot: first i from right with nums[i] < nums[i+1]
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # If no pivot, reverse whole array
        if i < 0:
            nums.reverse()
            return

        # 2) Find rightmost element greater than pivot
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1

        # 3) Swap pivot with that element
        nums[i], nums[j] = nums[j], nums[i]

        # 4) Reverse suffix to get smallest lexicographic order after pivot
        l, r = i + 1, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
