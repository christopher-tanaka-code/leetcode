from typing import List
from collections import Counter

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k != 0:
            return False

        cnt = Counter(nums)
        for x in sorted(cnt.keys()):
            c = cnt[x]
            if c == 0:
                continue

            # Need c copies of x..x+k-1
            for y in range(x, x + k):
                if cnt[y] < c:
                    return False
                cnt[y] -= c

        return True
