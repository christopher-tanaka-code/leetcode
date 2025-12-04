# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        node = root
        
        while True:
            # Go as left as possible
            while node:
                stack.append(node)
                node = node.left
            
            # Process the node
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            
            # Move to right subtree
            node = node.right
