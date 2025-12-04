# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # Helper function to compute the depth of the tree
        def get_depth(node: Optional[TreeNode]) -> int:
            depth = 0
            while node:
                node = node.left
                depth += 1
            return depth
        
        left_depth = get_depth(root.left)
        right_depth = get_depth(root.right)
        
        # If left and right subtree depths are equal, left subtree is perfect
        if left_depth == right_depth:
            # 2^left_depth nodes in the left subtree + 1 for root + recurse on right
            return (1 << left_depth) + self.countNodes(root.right)
        else:
            # Right subtree is perfect with height right_depth
            return (1 << right_depth) + self.countNodes(root.left)
