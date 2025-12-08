class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        # Convert both lists to sets to get distinct elements
        set1 = set(nums1)
        set2 = set(nums2)

        # Use set difference to find elements in one set but not in the other
        diff1 = list(set1 - set2)  # Elements in nums1 but not in nums2
        diff2 = list(set2 - set1)  # Elements in nums2 but not in nums1
        
        return [diff1, diff2]
