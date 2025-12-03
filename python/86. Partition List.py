class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Dummy heads for the two lists
        before_head = ListNode()
        after_head = ListNode()
        
        before = before_head
        after = after_head
        
        current = head
        
        # Traverse the original list
        while current:
            if current.val < x:
                before.next = current
                before = before.next
            else:
                after.next = current
                after = after.next
            current = current.next
        
        # End the "after" list to avoid cycles
        after.next = None
        
        # Connect the two lists
        before.next = after_head.next
        
        return before_head.next
