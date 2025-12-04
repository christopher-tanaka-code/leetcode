class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        def dfs(r, c, idx):
            # If we matched all letters
            if idx == len(word):
                return True
            # Check boundaries and current cell match
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[idx]:
                return False
            
            # Mark the cell as visited
            temp = board[r][c]
            board[r][c] = '#'
            
            # Explore all 4 directions
            found = (dfs(r+1, c, idx+1) or
                     dfs(r-1, c, idx+1) or
                     dfs(r, c+1, idx+1) or
                     dfs(r, c-1, idx+1))
            
            # Restore the cell
            board[r][c] = temp
            return found
        
        # Try to start DFS from every cell
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
