# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(float('-inf'))
        curr = head

        while curr:
            prev = dummy
            nxt = curr.next

            # Find where to insert current node in the sorted part
            while prev.next and prev.next.val < curr.val:
                prev = prev.next

            # Insert curr between prev and prev.next
            curr.next = prev.next
            prev.next = curr

            curr = nxt

        return dummy.next