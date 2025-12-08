class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd = head  # pointer to the first odd node
        even = head.next  # pointer to the first even node
        even_head = even  # store the head of even nodes to attach later
        
        while even and even.next:
            odd.next = even.next  # link current odd to next odd node
            odd = odd.next  # move odd pointer
            even.next = odd.next  # link current even to next even node
            even = even.next  # move even pointer
        
        odd.next = even_head  # attach even list after odd list
        return head
