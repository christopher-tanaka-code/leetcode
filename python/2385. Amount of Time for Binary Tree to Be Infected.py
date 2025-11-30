from collections import deque
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def amountOfTime(self, root: Optional['TreeNode'], start: int) -> int:
        parent = {}          # child_node -> parent_node
        start_node = None

        # Build parent pointers + find start node
        stack = [(root, None)]
        while stack:
            node, par = stack.pop()
            if not node:
                continue
            if par:
                parent[node] = par
            if node.val == start:
                start_node = node
            stack.append((node.left, node))
            stack.append((node.right, node))

        # BFS infection spread
        q = deque([start_node])
        seen = {start_node}
        minutes = -1

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                for nei in (node.left, node.right, parent.get(node)):
                    if nei and nei not in seen:
                        seen.add(nei)
                        q.append(nei)
            minutes += 1

        return minutes
