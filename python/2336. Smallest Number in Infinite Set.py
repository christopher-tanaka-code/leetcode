class SmallestInfiniteSet:

    def __init__(self):
        # Heap to store numbers added back
        self.min_heap = []
        # Set to quickly check if a number is already in the heap
        self.added_back = set()
        # Track the next smallest number in the infinite set
        self.next_num = 1

    def popSmallest(self) -> int:
        if self.min_heap:
            # Pop from heap if there are numbers added back
            smallest = heapq.heappop(self.min_heap)
            self.added_back.remove(smallest)
            return smallest
        else:
            # Otherwise, return the next number in sequence
            current = self.next_num
            self.next_num += 1
            return current

    def addBack(self, num: int) -> None:
        # Only add back numbers that are smaller than next_num and not already added
        if num < self.next_num and num not in self.added_back:
            heapq.heappush(self.min_heap, num)
            self.added_back.add(num)