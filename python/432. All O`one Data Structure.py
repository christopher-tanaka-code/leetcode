class Node:
    def __init__(self, count: int):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne:

    def __init__(self):
        self.key_to_node = {}

        self.head = Node(0)
        self.tail = Node(0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def inc(self, key: str) -> None:
        if key not in self.key_to_node:
            # Insert key with count 1
            if self.head.next != self.tail and self.head.next.count == 1:
                node = self.head.next
            else:
                node = Node(1)
                self._insert_after(self.head, node)

            node.keys.add(key)
            self.key_to_node[key] = node
            return

        current = self.key_to_node[key]
        new_count = current.count + 1

        if current.next != self.tail and current.next.count == new_count:
            next_node = current.next
        else:
            next_node = Node(new_count)
            self._insert_after(current, next_node)

        next_node.keys.add(key)
        self.key_to_node[key] = next_node

        current.keys.remove(key)
        if not current.keys:
            self._remove_node(current)

    def dec(self, key: str) -> None:
        current = self.key_to_node[key]

        if current.count == 1:
            # Remove key completely
            del self.key_to_node[key]
        else:
            new_count = current.count - 1

            if current.prev != self.head and current.prev.count == new_count:
                prev_node = current.prev
            else:
                prev_node = Node(new_count)
                self._insert_after(current.prev, prev_node)

            prev_node.keys.add(key)
            self.key_to_node[key] = prev_node

        current.keys.remove(key)
        if not current.keys:
            self._remove_node(current)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""

        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""

        return next(iter(self.head.next.keys))

    def _insert_after(self, prev_node: Node, new_node: Node) -> None:
        next_node = prev_node.next

        prev_node.next = new_node
        new_node.prev = prev_node

        new_node.next = next_node
        next_node.prev = new_node

    def _remove_node(self, node: Node) -> None:
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node