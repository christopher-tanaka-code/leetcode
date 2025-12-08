class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_length = 0

        def dfs(node, is_left, length):
            if not node:
                return
            
            # Update the global maximum length
            self.max_length = max(self.max_length, length)
            
            # If we came from left, go right next; if from right, go left next
            if is_left:
                dfs(node.right, False, length + 1)  # move right next
                dfs(node.left, True, 1)  # reset if continuing left
            else:
                dfs(node.left, True, length + 1)   # move left next
                dfs(node.right, False, 1)  # reset if continuing right
        
        # Start DFS from root in both directions
        dfs(root.left, True, 1)  # start going left
        dfs(root.right, False, 1)  # start going right
        
        return self.max_length
