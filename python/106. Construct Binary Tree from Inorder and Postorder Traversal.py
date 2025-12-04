# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        # Correct hashmap creation
        index_map = {v: i for i, v in enumerate(inorder)}

        self.post_idx = len(postorder) - 1

        def build(left, right):
            if left > right:
                return None

            root_val = postorder[self.post_idx]
            self.post_idx -= 1

            root = TreeNode(root_val)
            idx = index_map[root_val]

            # build right subtree first
            root.right = build(idx + 1, right)
            # then left subtree
            root.left = build(left, idx - 1)

            return root

        return build(0, len(inorder) - 1)
