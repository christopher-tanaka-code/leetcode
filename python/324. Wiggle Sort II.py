from typing import List
import random

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        def nth_element(k: int) -> int:
            arr = nums[:]

            def select(left: int, right: int, k_smallest: int) -> int:
                while True:
                    if left == right:
                        return arr[left]

                    pivot_index = random.randint(left, right)
                    pivot = arr[pivot_index]

                    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
                    store = left

                    for i in range(left, right):
                        if arr[i] < pivot:
                            arr[store], arr[i] = arr[i], arr[store]
                            store += 1

                    equal = store
                    for i in range(store, right):
                        if arr[i] == pivot:
                            arr[equal], arr[i] = arr[i], arr[equal]
                            equal += 1

                    arr[equal], arr[right] = arr[right], arr[equal]

                    if k_smallest < store:
                        right = store - 1
                    elif k_smallest > equal:
                        left = equal + 1
                    else:
                        return pivot

            return select(0, len(arr) - 1, k)

        n = len(nums)
        median = nth_element(n // 2)

        def new_index(i: int) -> int:
            return (1 + 2 * i) % (n | 1)

        left, i, right = 0, 0, n - 1

        while i <= right:
            ni = new_index(i)
            if nums[ni] > median:
                nl = new_index(left)
                nums[nl], nums[ni] = nums[ni], nums[nl]
                left += 1
                i += 1
            elif nums[ni] < median:
                nr = new_index(right)
                nums[nr], nums[ni] = nums[ni], nums[nr]
                right -= 1
            else:
                i += 1