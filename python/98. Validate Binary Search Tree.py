# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, lower=float('-inf'), upper=float('inf')) -> bool:
            if not node:
                return True
            
            val = node.val
            if val <= lower or val >= upper:
                return False
            
            # Check right subtree with updated lower bound
            if not helper(node.right, val, upper):
                return False
            # Check left subtree with updated upper bound
            if not helper(node.left, lower, val):
                return False
            
            return True
        
        return helper(root)
