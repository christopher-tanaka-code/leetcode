from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(
        self,
        nums: List[int],
        indexDiff: int,
        valueDiff: int
    ) -> bool:
        if valueDiff < 0:
            return False

        # Bucket size: valueDiff + 1
        # Any two numbers in the same bucket differ by at most valueDiff.
        bucket_size = valueDiff + 1
        buckets = {}

        def get_bucket_id(x: int) -> int:
            # Works correctly for negative numbers too.
            return x // bucket_size

        for i, num in enumerate(nums):
            bucket_id = get_bucket_id(num)

            # 1) Same bucket => guaranteed abs difference <= valueDiff
            if bucket_id in buckets:
                return True

            # 2) Neighbor buckets may also contain a valid number
            if (
                bucket_id - 1 in buckets
                and abs(num - buckets[bucket_id - 1]) <= valueDiff
            ):
                return True

            if (
                bucket_id + 1 in buckets
                and abs(num - buckets[bucket_id + 1]) <= valueDiff
            ):
                return True

            # Insert current number into its bucket
            buckets[bucket_id] = num

            # Maintain sliding window of size indexDiff
            if i >= indexDiff:
                old_num = nums[i - indexDiff]
                old_bucket_id = get_bucket_id(old_num)
                del buckets[old_bucket_id]

        return False
