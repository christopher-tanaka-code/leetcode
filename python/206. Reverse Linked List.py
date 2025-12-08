class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            nxt = current.next  # temporarily store the next node
            current.next = prev  # reverse the current node's pointer
            prev = current       # move prev forward
            current = nxt        # move current forward
        
        return prev  # prev becomes the new head
