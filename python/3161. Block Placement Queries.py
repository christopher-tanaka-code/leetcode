from typing import List, Optional

class Fenwick:
    # 1-indexed Fenwick tree for counts
    def __init__(self, n: int):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i: int, delta: int) -> None:
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def sum(self, i: int) -> int:
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def find_by_order(self, k: int) -> int:
        """Return smallest idx such that prefix_sum(idx) >= k (k is 1-based)."""
        idx = 0
        bitmask = 1 << (self.n.bit_length() - 1)
        while bitmask:
            nxt = idx + bitmask
            if nxt <= self.n and self.bit[nxt] < k:
                idx = nxt
                k -= self.bit[nxt]
            bitmask >>= 1
        return idx + 1


class SegTreeMax:
    # iterative segment tree for range max on [1..n]
    def __init__(self, n: int):
        N = 1
        while N < n + 1:
            N <<= 1
        self.N = N
        self.t = [0] * (2 * N)

    def update(self, i: int, val: int) -> None:
        p = i + self.N
        self.t[p] = val
        p //= 2
        while p:
            self.t[p] = self.t[2 * p] if self.t[2 * p] >= self.t[2 * p + 1] else self.t[2 * p + 1]
            p //= 2

    def query(self, l: int, r: int) -> int:
        if l > r:
            return 0
        l += self.N
        r += self.N
        res = 0
        while l <= r:
            if l & 1:
                if self.t[l] > res:
                    res = self.t[l]
                l += 1
            if not (r & 1):
                if self.t[r] > res:
                    res = self.t[r]
                r -= 1
            l //= 2
            r //= 2
        return res


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        M = max(q[1] for q in queries)  # max coordinate used in any query
        fw = Fenwick(M)
        seg = SegTreeMax(M)

        def predecessor(x: int) -> int:
            """Greatest obstacle position <= x, or 0 if none."""
            if x <= 0:
                return 0
            cnt = fw.sum(x)
            if cnt == 0:
                return 0
            return fw.find_by_order(cnt)

        def successor(x: int) -> Optional[int]:
            """Smallest obstacle position > x, or None if none."""
            cnt_le = fw.sum(x)
            total = fw.sum(M)
            if cnt_le == total:
                return None
            return fw.find_by_order(cnt_le + 1)

        results = []

        for q in queries:
            if q[0] == 1:
                x = q[1]
                prev = predecessor(x)      # x not present yet (guaranteed)
                nxt = successor(x)

                fw.add(x, 1)
                seg.update(x, x - prev)   # new gap ending at x

                if nxt is not None:
                    seg.update(nxt, nxt - x)  # nxt's predecessor changes to x
            else:
                x, sz = q[1], q[2]
                prev = predecessor(x)
                internal_best = seg.query(1, x)  # best gap whose right endpoint is an obstacle <= x
                tail_gap = x - prev              # last gap up to boundary x
                results.append(max(internal_best, tail_gap) >= sz)

        return results
