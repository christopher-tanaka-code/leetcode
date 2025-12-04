# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = None
        
        def helper(node):
            if not node:
                return
            
            # Reverse preorder: right → left → node
            helper(node.right)
            helper(node.left)
            
            # Rewire pointers
            node.right = self.prev
            node.left = None
            
            # Move prev to current
            self.prev = node
        
        helper(root)
