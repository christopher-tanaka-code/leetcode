class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row):
            nonlocal count
            if row == n:
                count += 1
                return
            
            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                # Place the queen
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                
                backtrack(row + 1)
                
                # Remove the queen (backtrack)
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
        
        count = 0
        cols = set()      # Columns where queens are placed
        diag1 = set()     # Main diagonals (row - col)
        diag2 = set()     # Anti-diagonals (row + col)
        
        backtrack(0)
        return count
