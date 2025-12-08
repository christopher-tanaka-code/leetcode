class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total_sum = sum(nums)  # total sum of array
        left_sum = 0

        for i, num in enumerate(nums):
            # Right sum = total_sum - left_sum - num
            if left_sum == (total_sum - left_sum - num):
                return i
            left_sum += num

        return -1
