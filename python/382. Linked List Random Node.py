import random
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        result = None
        current = self.head
        count = 0

        while current:
            count += 1

            # Choose current node with probability 1 / count
            if random.randint(1, count) == 1:
                result = current.val

            current = current.next

        return result