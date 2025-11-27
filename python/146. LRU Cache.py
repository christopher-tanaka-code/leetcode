class Node:
    __slots__ = ("key", "val", "prev", "next")
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # key -> Node

        # dummy sentinels
        self.head = Node()  # MRU side
        self.tail = Node()  # LRU side
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        p, n = node.prev, node.next
        p.next = n
        n.prev = p

    def _add_to_front(self, node: Node) -> None:
        # insert node right after head (MRU)
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _move_to_front(self, node: Node) -> None:
        self._remove(node)
        self._add_to_front(node)

    def _pop_lru(self) -> Node:
        # remove node just before tail
        lru = self.tail.prev
        self._remove(lru)
        return lru

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if not node:
            return -1
        self._move_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)

        if node:
            node.val = value
            self._move_to_front(node)
            return

        new_node = Node(key, value)
        self.cache[key] = new_node
        self._add_to_front(new_node)

        if len(self.cache) > self.cap:
            lru = self._pop_lru()
            del self.cache[lru.key]
