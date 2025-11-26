from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional['ListNode'], k: int) -> Optional['ListNode']:
        if not head or k == 1:
            return head

        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # Find the k-th node from group_prev
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next  # fewer than k nodes left

            group_next = kth.next  # node after the group

            # Reverse the group [group_prev.next ... kth]
            prev = group_next
            curr = group_prev.next
            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # Reconnect reversed group back to list
            old_group_start = group_prev.next  # becomes the tail after reversal
            group_prev.next = kth             # kth is new head of the reversed group
            group_prev = old_group_start      # move to tail for next iteration
