from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []  # If tree is empty, return empty list

        result = []
        queue = deque([root])  # Initialize queue with root node

        while queue:
            level_size = len(queue)  # Number of nodes at current level
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()  # Pop node from queue
                current_level.append(node.val)  # Add its value to current level

                # Add child nodes to queue if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(current_level)  # Append current level to result

        return result
