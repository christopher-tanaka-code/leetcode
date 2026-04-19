# Below is the interface for Iterator, which is already defined for you.
# class Iterator:
#     def __init__(self, nums: List[int]):
#         """
#         Initializes an iterator object to the beginning of a list.
#         """
#     def hasNext(self) -> bool:
#         """
#         Returns true if the iteration has more elements.
#         """
#     def next(self) -> int:
#         """
#         Returns the next element in the iteration.
#         """

class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.next_val = iterator.next() if iterator.hasNext() else None

    def peek(self):
        return self.next_val

    def next(self):
        val = self.next_val
        self.next_val = self.iterator.next() if self.iterator.hasNext() else None
        return val

    def hasNext(self):
        return self.next_val is not None