class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')
        
        for num in nums:
            if num <= first:
                first = num  # update first smallest
            elif num <= second:
                second = num  # update second smallest
            else:
                # found a number greater than both first and second
                return True
        
        return False
