# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy       # prev points to the last node before duplicates
        curr = head        # current pointer

        while curr:
            # Detect duplicates by checking if current value repeats
            if curr.next and curr.val == curr.next.val:
                # Skip all nodes with this value
                duplicate_val = curr.val
                while curr and curr.val == duplicate_val:
                    curr = curr.next
                prev.next = curr   # Remove all duplicates
            else:
                prev = prev.next   # Move prev only if no duplicate detected
                curr = curr.next

        return dummy.next
