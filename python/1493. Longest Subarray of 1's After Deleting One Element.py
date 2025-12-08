class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zeros = 0
        longest = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            
            # shrink window until at most one zero
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            # length minus 1 because we must delete one element
            longest = max(longest, right - left)

        return longest
