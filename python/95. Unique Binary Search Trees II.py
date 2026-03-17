# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from functools import lru_cache
from typing import List, Optional

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @lru_cache(None)
        def build(left: int, right: int):
            if left > right:
                return [None]

            trees = []

            for root_val in range(left, right + 1):
                left_trees = build(left, root_val - 1)
                right_trees = build(root_val + 1, right)

                for left_subtree in left_trees:
                    for right_subtree in right_trees:
                        root = TreeNode(root_val)
                        root.left = left_subtree
                        root.right = right_subtree
                        trees.append(root)

            return trees

        return build(1, n)