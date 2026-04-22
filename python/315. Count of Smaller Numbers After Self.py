from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = [0] * n
        arr = list(enumerate(nums))  # (original_index, value)

        def merge_sort(left: int, right: int) -> None:
            if right - left <= 1:
                return

            mid = (left + right) // 2
            merge_sort(left, mid)
            merge_sort(mid, right)

            merged = []
            i, j = left, mid
            right_smaller = 0

            while i < mid and j < right:
                if arr[j][1] < arr[i][1]:
                    merged.append(arr[j])
                    right_smaller += 1
                    j += 1
                else:
                    counts[arr[i][0]] += right_smaller
                    merged.append(arr[i])
                    i += 1

            while i < mid:
                counts[arr[i][0]] += right_smaller
                merged.append(arr[i])
                i += 1

            while j < right:
                merged.append(arr[j])
                j += 1

            arr[left:right] = merged

        merge_sort(0, n)
        return counts