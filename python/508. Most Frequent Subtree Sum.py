from typing import Optional, List
from collections import Counter

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        count = Counter()

        def dfs(node):
            if not node:
                return 0

            total = node.val + dfs(node.left) + dfs(node.right)
            count[total] += 1
            return total

        dfs(root)

        max_freq = max(count.values())
        return [s for s, freq in count.items() if freq == max_freq]