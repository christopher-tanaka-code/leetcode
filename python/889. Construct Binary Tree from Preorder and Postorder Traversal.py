from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional['TreeNode']:
        n = len(preorder)
        pos = {v: i for i, v in enumerate(postorder)}  # value -> index in postorder

        def build(pre_l: int, pre_r: int, post_l: int, post_r: int) -> Optional['TreeNode']:
            if pre_l > pre_r:
                return None

            root = TreeNode(preorder[pre_l])
            if pre_l == pre_r:
                return root

            # The next preorder value is the root of the left subtree
            left_root_val = preorder[pre_l + 1]
            left_root_idx_in_post = pos[left_root_val]
            left_size = left_root_idx_in_post - post_l + 1

            root.left = build(
                pre_l + 1, pre_l + left_size,
                post_l, left_root_idx_in_post
            )
            root.right = build(
                pre_l + left_size + 1, pre_r,
                left_root_idx_in_post + 1, post_r - 1
            )
            return root

        return build(0, n - 1, 0, n - 1)
