from typing import List, Tuple

class MyHashMap:
    def __init__(self):
        # A prime-ish bucket size to reduce collisions
        self._size = 2069
        self._buckets: List[List[Tuple[int, int]]] = [[] for _ in range(self._size)]

    def _idx(self, key: int) -> int:
        return key % self._size

    def put(self, key: int, value: int) -> None:
        b = self._buckets[self._idx(key)]
        for i, (k, v) in enumerate(b):
            if k == key:
                b[i] = (key, value)  # update
                return
        b.append((key, value))  # insert new

    def get(self, key: int) -> int:
        b = self._buckets[self._idx(key)]
        for k, v in b:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        b = self._buckets[self._idx(key)]
        for i, (k, v) in enumerate(b):
            if k == key:
                b.pop(i)
                return
