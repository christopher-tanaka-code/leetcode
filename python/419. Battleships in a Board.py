from typing import List

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        ships = 0

        for r in range(m):
            for c in range(n):
                if board[r][c] == ".":
                    continue

                # Not the start if there is another part of the ship above
                if r > 0 and board[r - 1][c] == "X":
                    continue

                # Not the start if there is another part of the ship on the left
                if c > 0 and board[r][c - 1] == "X":
                    continue

                ships += 1

        return ships