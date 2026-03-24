from typing import List

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        mn = min(nums)
        mx = max(nums)

        if mn == mx:
            return 0

        # Minimum possible maximum gap
        bucket_size = max(1, (mx - mn + n - 2) // (n - 1))  # ceil((mx - mn) / (n - 1))
        bucket_count = (mx - mn) // bucket_size + 1

        buckets_min = [float("inf")] * bucket_count
        buckets_max = [float("-inf")] * bucket_count
        used = [False] * bucket_count

        # Put each number into a bucket
        for num in nums:
            idx = (num - mn) // bucket_size
            buckets_min[idx] = min(buckets_min[idx], num)
            buckets_max[idx] = max(buckets_max[idx], num)
            used[idx] = True

        max_gap = 0
        prev_max = mn

        # Scan buckets to find the largest gap between consecutive non-empty buckets
        for i in range(bucket_count):
            if not used[i]:
                continue
            max_gap = max(max_gap, buckets_min[i] - prev_max)
            prev_max = buckets_max[i]

        return max_gap
