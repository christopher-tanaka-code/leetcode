from typing import Optional, List

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []
        node = root

        prev = None
        count = 0
        max_count = 0

        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()

            if prev is not None and node.val == prev:
                count += 1
            else:
                prev = node.val
                count = 1

            if count > max_count:
                max_count = count
                ans = [node.val]
            elif count == max_count:
                ans.append(node.val)

            node = node.right

        return ans