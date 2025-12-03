class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # 1. Insert cloned nodes after each original node
        curr = head
        while curr:
            nxt = curr.next
            curr.next = Node(curr.val)
            curr.next.next = nxt
            curr = nxt
        
        # 2. Assign random pointers for cloned nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        # 3. Separate the original list and the cloned list
        curr = head
        pseudo_head = head.next
        copy_curr = pseudo_head
        
        while curr:
            curr.next = curr.next.next
            copy_curr.next = copy_curr.next.next if copy_curr.next else None
            curr = curr.next
            copy_curr = copy_curr.next
        
        return pseudo_head
