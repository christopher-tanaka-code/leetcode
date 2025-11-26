from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: Optional['TreeNode']) -> List[int]:
        res: List[int] = []
        stack: List['TreeNode'] = []
        cur = root
        last_visited = None

        while cur or stack:
            # Go as left as possible
            while cur:
                stack.append(cur)
                cur = cur.left

            node = stack[-1]
            # If right subtree exists and not processed yet, traverse it
            if node.right and last_visited is not node.right:
                cur = node.right
            else:
                res.append(node.val)
                last_visited = stack.pop()

        return res
