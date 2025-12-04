class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        curr = root  # Current level head
        
        while curr:
            dummy = Node(0)  # Dummy head for next level
            tail = dummy     # Tail pointer builds next-level chain
            
            # Traverse the current level
            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next
                
                curr = curr.next  # Move within the level
            
            # Move to next level
            curr = dummy.next
        
        return root
