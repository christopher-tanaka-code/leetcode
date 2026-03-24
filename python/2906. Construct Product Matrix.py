from typing import List

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        n, m = len(grid), len(grid[0])
        k = n * m

        # Flatten grid so we can do 1D prefix/suffix product.
        arr = [0] * k
        idx = 0
        for i in range(n):
            for j in range(m):
                arr[idx] = grid[i][j] % MOD
                idx += 1

        # left[i] = product of arr[0..i-1] mod MOD
        left = [1] * k
        for i in range(1, k):
            left[i] = (left[i - 1] * arr[i - 1]) % MOD

        # right = running suffix product from the right
        ans = [[0] * m for _ in range(n)]
        right = 1

        for i in range(k - 1, -1, -1):
            prod_except_self = (left[i] * right) % MOD
            ans[i // m][i % m] = prod_except_self
            right = (right * arr[i]) % MOD

        return ans
