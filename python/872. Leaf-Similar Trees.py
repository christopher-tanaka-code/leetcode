class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeaves(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [node.val]
            return getLeaves(node.left) + getLeaves(node.right)

        return getLeaves(root1) == getLeaves(root2)
