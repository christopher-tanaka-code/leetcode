from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)

        # Custom object to get desired ordering in a min-heap:
        # "worse" = smaller freq OR same freq but lexicographically larger
        class Word:
            __slots__ = ("w", "f")
            def __init__(self, w: str, f: int):
                self.w = w
                self.f = f

            def __lt__(self, other: "Word") -> bool:
                if self.f != other.f:
                    return self.f < other.f          # lower frequency is worse
                return self.w > other.w              # lexicographically larger is worse

        heap = []
        for w, f in freq.items():
            heapq.heappush(heap, Word(w, f))
            if len(heap) > k:
                heapq.heappop(heap)

        # Heap has k best elements but not in final order; sort them properly:
        # frequency desc, word asc
        heap.sort(key=lambda x: (-x.f, x.w))
        return [x.w for x in heap]
