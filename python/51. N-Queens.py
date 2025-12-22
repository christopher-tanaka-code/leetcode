from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res: List[List[str]] = []
        cols = [False] * n              # col is occupied
        diag1 = [False] * (2 * n - 1)   # r - c + (n-1)
        diag2 = [False] * (2 * n - 1)   # r + c
        placement = [-1] * n            # placement[r] = c

        def backtrack(r: int) -> None:
            if r == n:
                board = []
                for rr in range(n):
                    c = placement[rr]
                    row = "." * c + "Q" + "." * (n - c - 1)
                    board.append(row)
                res.append(board)
                return

            for c in range(n):
                d1 = r - c + (n - 1)
                d2 = r + c
                if cols[c] or diag1[d1] or diag2[d2]:
                    continue

                placement[r] = c
                cols[c] = diag1[d1] = diag2[d2] = True
                backtrack(r + 1)
                cols[c] = diag1[d1] = diag2[d2] = False
                placement[r] = -1

        backtrack(0)
        return res
