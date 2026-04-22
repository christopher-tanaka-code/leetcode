from typing import List

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        def sort_and_count(lo: int, hi: int) -> int:
            if hi - lo <= 1:
                return 0

            mid = (lo + hi) // 2
            count = sort_and_count(lo, mid) + sort_and_count(mid, hi)

            j = k = mid
            for left_val in prefix[lo:mid]:
                while k < hi and prefix[k] - left_val < lower:
                    k += 1
                while j < hi and prefix[j] - left_val <= upper:
                    j += 1
                count += j - k

            prefix[lo:hi] = sorted(prefix[lo:hi])
            return count

        return sort_and_count(0, len(prefix))