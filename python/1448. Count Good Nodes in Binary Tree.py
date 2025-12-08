class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0
            # Check if current node is good
            count = 1 if node.val >= max_val else 0
            # Update the max value along the path
            new_max = max(max_val, node.val)
            # Recursively check left and right children
            count += dfs(node.left, new_max)
            count += dfs(node.right, new_max)
            return count

        # Start DFS with root and its value as the initial max
        return dfs(root, root.val)
