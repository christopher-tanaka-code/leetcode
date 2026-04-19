# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        vals = []

        def dfs(node):
            if not node:
                vals.append("N")
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(vals)

    def deserialize(self, data):
        vals = iter(data.split(","))

        def dfs():
            val = next(vals)
            if val == "N":
                return None

            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()