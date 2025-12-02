from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])

        def live_neighbors(r: int, c: int) -> int:
            cnt = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and board[nr][nc] in (1, 2):
                        cnt += 1
            return cnt

        # 1st pass: write transition markers (2, 3)
        for r in range(m):
            for c in range(n):
                ln = live_neighbors(r, c)
                if board[r][c] == 1:
                    if ln < 2 or ln > 3:
                        board[r][c] = 2  # live -> dead
                else:  # board[r][c] == 0
                    if ln == 3:
                        board[r][c] = 3  # dead -> live

        # 2nd pass: finalize states
        for r in range(m):
            for c in range(n):
                if board[r][c] == 2:
                    board[r][c] = 0
                elif board[r][c] == 3:
                    board[r][c] = 1
