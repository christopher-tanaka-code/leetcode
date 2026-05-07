from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        values = []
        stack = [root]

        # Preorder traversal: root, left, right
        while stack:
            node = stack.pop()
            values.append(str(node.val))

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return ",".join(values)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        preorder = list(map(int, data.split(",")))

        root = TreeNode(preorder[0])
        stack = [root]

        for value in preorder[1:]:
            node = TreeNode(value)

            if value < stack[-1].val:
                stack[-1].left = node
                stack.append(node)
            else:
                parent = None

                while stack and value > stack[-1].val:
                    parent = stack.pop()

                parent.right = node
                stack.append(node)

        return root