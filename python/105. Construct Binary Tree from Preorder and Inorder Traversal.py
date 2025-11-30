from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional['TreeNode']:
        if not preorder or not inorder:
            return None

        pos = {v: i for i, v in enumerate(inorder)}
        pre_i = 0

        def helper(l: int, r: int) -> Optional['TreeNode']:
            nonlocal pre_i
            if l > r:
                return None

            root_val = preorder[pre_i]
            pre_i += 1
            root = TreeNode(root_val)

            mid = pos[root_val]
            root.left = helper(l, mid - 1)
            root.right = helper(mid + 1, r)
            return root

        return helper(0, len(inorder) - 1)
