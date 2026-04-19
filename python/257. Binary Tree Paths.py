from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []

        def dfs(node: Optional[TreeNode], path: str) -> None:
            if not node:
                return

            if not node.left and not node.right:
                result.append(path + str(node.val))
                return

            new_path = path + str(node.val) + "->"
            dfs(node.left, new_path)
            dfs(node.right, new_path)

        dfs(root, "")
        return result