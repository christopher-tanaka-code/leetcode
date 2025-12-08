class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1 # base case to handle exact target sum from root

        def dfs(node, curr_sum):
            if not node:
                return 0
            
            curr_sum += node.val
            # Number of valid paths ending at current node
            count = prefix_sums[curr_sum - targetSum]
            
            # Update prefix sums for child nodes
            prefix_sums[curr_sum] += 1
            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)
            prefix_sums[curr_sum] -= 1  # backtrack
            
            return count

        return dfs(root, 0)