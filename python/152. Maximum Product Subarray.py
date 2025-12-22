from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # cur_max = max product ending at current index
        # cur_min = min product ending at current index (needed because negative flips)
        cur_max = cur_min = ans = nums[0]

        for x in nums[1:]:
            if x < 0:
                cur_max, cur_min = cur_min, cur_max  # flip before multiplying

            cur_max = max(x, cur_max * x)
            cur_min = min(x, cur_min * x)

            ans = max(ans, cur_max)

        return ans
