class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = {}
        operations = 0
        
        for x in nums:
            target = k - x
            # If target exists, pair it with x
            if count.get(target, 0) > 0:
                operations += 1
                count[target] -= 1
            else:
                # Otherwise store x
                count[x] = count.get(x, 0) + 1
        
        return operations
