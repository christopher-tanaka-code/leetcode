# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        path = []

        def dfs(node, remaining):
            if not node:
                return

            path.append(node.val)

            # Check if it's a leaf and the path sum matches
            if not node.left and not node.right and remaining == node.val:
                result.append(path[:])
            else:
                dfs(node.left, remaining - node.val)
                dfs(node.right, remaining - node.val)

            path.pop()  # backtrack

        dfs(root, targetSum)
        return result