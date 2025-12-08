class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: if there's only one node, return None
        if not head or not head.next:
            return None

        slow = head
        fast = head
        prev = None  # To keep track of the node before slow
        
        # Move fast pointer two steps and slow pointer one step
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        
        # Delete the middle node
        prev.next = slow.next
        
        return head
