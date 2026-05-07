# Definition for a Node.
# class Node:
#     def __init__(self, val, prev, next, child):
#         self.val = val
#         self.prev = prev
#         self.next = next
#         self.child = child

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        current = head

        while current:
            if current.child:
                child_head = current.child
                next_node = current.next

                # Find the tail of the child list
                child_tail = child_head
                while child_tail.next:
                    child_tail = child_tail.next

                # Connect current -> child_head
                current.next = child_head
                child_head.prev = current
                current.child = None

                # Connect child_tail -> next_node
                if next_node:
                    child_tail.next = next_node
                    next_node.prev = child_tail

            current = current.next

        return head