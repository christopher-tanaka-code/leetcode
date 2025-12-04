# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        
        def helper(node):
            if not node:
                return 0
            
            # Max path sum on left and right; ignore negative sums
            left_max = max(helper(node.left), 0)
            right_max = max(helper(node.right), 0)
            
            # Check if the current node is the "peak" of the path
            current_sum = node.val + left_max + right_max
            self.max_sum = max(self.max_sum, current_sum)
            
            # Return the max path sum extending to parent
            return node.val + max(left_max, right_max)
        
        helper(root)
        return self.max_sum
