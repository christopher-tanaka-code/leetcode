import heapq
from dataclasses import dataclass

@dataclass(frozen=True)
class Better:  # for `rest`: heap top is BEST remaining
    score: int
    name: str

    def __lt__(self, other: "Better") -> bool:
        if self.score != other.score:
            return self.score > other.score       # higher score first
        return self.name < other.name             # lex smaller first


@dataclass(frozen=True)
class Worse:   # for `top`: heap top is WORST among the best-k
    score: int
    name: str

    def __lt__(self, other: "Worse") -> bool:
        if self.score != other.score:
            return self.score < other.score       # lower score is worse
        return self.name > other.name             # lex larger is worse


class SORTracker:
    def __init__(self):
        self.k = 0               # number of get() calls so far
        self.top = []            # heap of Worse, size == k
        self.rest = []           # heap of Better

    def add(self, name: str, score: int) -> None:
        if self.k == 0:
            heapq.heappush(self.rest, Better(score, name))
            return

        kth = self.top[0]  # current k-th best (worst among top-k)
        is_better_than_kth = (score > kth.score) or (score == kth.score and name < kth.name)

        if is_better_than_kth:
            heapq.heappush(self.top, Worse(score, name))
            demoted = heapq.heappop(self.top)  # demote worst from top
            heapq.heappush(self.rest, Better(demoted.score, demoted.name))
        else:
            heapq.heappush(self.rest, Better(score, name))

    def get(self) -> str:
        self.k += 1
        promoted = heapq.heappop(self.rest)          # best remaining becomes part of top-k
        heapq.heappush(self.top, Worse(promoted.score, promoted.name))
        return self.top[0].name                      # k-th best
