# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        # Stack to simulate the in-order traversal
        self.stack = []
        # Initialize the stack with the leftmost path
        self._push_left_branch(root)
    
    def _push_left_branch(self, node: Optional[TreeNode]):
        """Push all left children of a node onto the stack"""
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        # Pop the top node (next smallest)
        node = self.stack.pop()
        val = node.val
        # If the node has a right child, push its leftmost path onto the stack
        if node.right:
            self._push_left_branch(node.right)
        return val

    def hasNext(self) -> bool:
        # There is a next element if the stack is not empty
        return len(self.stack) > 0
