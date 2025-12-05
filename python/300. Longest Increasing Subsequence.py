from typing import List
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []  # This will store the smallest tail of all increasing subsequences
        for num in nums:
            # Find the index where 'num' can replace in 'sub'
            i = bisect.bisect_left(sub, num)
            if i == len(sub):
                sub.append(num)  # If num is bigger than all, extend the subsequence
            else:
                sub[i] = num  # Replace existing value to maintain the smallest tail
        return len(sub)
