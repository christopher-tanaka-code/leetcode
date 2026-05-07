class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)

        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])

        ans = [0] * n
        start = 0
        current_max = nums[0]

        for i in range(n):
            current_max = max(current_max, nums[i])

            # If every value on the left side is <= every value on the right side,
            # then there is no valid jump crossing this boundary.
            if i == n - 1 or current_max <= suffix_min[i + 1]:
                for j in range(start, i + 1):
                    ans[j] = current_max

                if i + 1 < n:
                    start = i + 1
                    current_max = nums[i + 1]

        return ans