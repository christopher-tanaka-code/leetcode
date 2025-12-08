class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        # If key is smaller, go left
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        # If key is larger, go right
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node found
            if not root.left:
                return root.right  # Replace with right child
            elif not root.right:
                return root.left   # Replace with left child
            else:
                # Node has two children, find inorder successor
                successor = root.right
                while successor.left:
                    successor = successor.left
                # Copy successor value to root
                root.val = successor.val
                # Delete the successor
                root.right = self.deleteNode(root.right, successor.val)
        
        return root
