from typing import List

class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        # 1-indexed arrays for convenience
        sum_path = [0] * (n + 1)
        for i in range(1, n + 1):
            sum_path[i] = cost[i - 1]

        ans = 0
        # internal nodes are 1 .. n//2 in a perfect binary tree stored this way
        for i in range(n // 2, 0, -1):
            left, right = 2 * i, 2 * i + 1
            ans += abs(sum_path[left] - sum_path[right])
            sum_path[i] += max(sum_path[left], sum_path[right])

        return ans
