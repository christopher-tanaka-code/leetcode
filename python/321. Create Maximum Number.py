from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def max_subsequence(nums: List[int], k: int) -> List[int]:
            drop = len(nums) - k
            stack = []

            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)

            return stack[:k]

        def greater(nums1: List[int], i: int, nums2: List[int], j: int) -> bool:
            while i < len(nums1) and j < len(nums2) and nums1[i] == nums2[j]:
                i += 1
                j += 1
            if j == len(nums2):
                return True
            if i < len(nums1) and nums1[i] > nums2[j]:
                return True
            return False

        def merge(seq1: List[int], seq2: List[int]) -> List[int]:
            i = j = 0
            merged = []

            while i < len(seq1) or j < len(seq2):
                if greater(seq1, i, seq2, j):
                    merged.append(seq1[i])
                    i += 1
                else:
                    merged.append(seq2[j])
                    j += 1

            return merged

        best = []
        start = max(0, k - len(nums2))
        end = min(k, len(nums1))

        for i in range(start, end + 1):
            part1 = max_subsequence(nums1, i)
            part2 = max_subsequence(nums2, k - i)
            candidate = merge(part1, part2)
            if candidate > best:
                best = candidate

        return best