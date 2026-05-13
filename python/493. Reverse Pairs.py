from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(left: int, right: int) -> int:
            if right - left <= 1:
                return 0

            mid = (left + right) // 2
            count = merge_sort(left, mid) + merge_sort(mid, right)

            j = mid
            for i in range(left, mid):
                while j < right and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - mid

            temp = []
            i, j = left, mid

            while i < mid and j < right:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1

            temp.extend(nums[i:mid])
            temp.extend(nums[j:right])
            nums[left:right] = temp

            return count

        return merge_sort(0, len(nums))