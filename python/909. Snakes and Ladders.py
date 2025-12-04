from collections import deque
from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        # Helper function: convert board coordinates (row, col) to square number
        def rc_to_square(r, c):
            # Board is numbered from bottom-left
            row = n - 1 - r
            if row % 2 == 0:  # left to right
                return row * n + c + 1
            else:  # right to left
                return row * n + (n - 1 - c) + 1
        
        # Helper function: convert square number to board coordinates
        def square_to_rc(square):
            square -= 1
            row = n - 1 - (square // n)
            col = square % n
            if (n - 1 - row) % 2 == 1:  # right to left row
                col = n - 1 - col
            return row, col

        # BFS setup
        visited = set()
        q = deque([(1, 0)])  # (current square, moves)

        while q:
            square, moves = q.popleft()
            
            if square == n * n:
                return moves  # reached the last square
            
            for next_square in range(square + 1, min(square + 6, n * n) + 1):
                r, c = square_to_rc(next_square)
                if board[r][c] != -1:
                    next_square = board[r][c]  # take the snake or ladder
                
                if next_square not in visited:
                    visited.add(next_square)
                    q.append((next_square, moves + 1))
        
        return -1  # if unreachable
